import os
import praw
import time
import logging
import psycopg2
from dotenv import load_dotenv
from utils import update_user_info, add_posts, add_comments


# Настройка логгера
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение переменных окружения
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')

reddit_client_id = os.getenv('REDDIT_CLIENT_ID')
reddit_client_secret = os.getenv('REDDIT_CLIENT_SECRET')
reddit_password = os.getenv('REDDIT_PASSWORD')
reddit_user_agent = os.getenv('REDDIT_USER_AGENT')
reddit_username = os.getenv('REDDIT_USERNAME')

max_retries = int(os.getenv('MAX_RETRIES', '3'))
retry_delay = int(os.getenv('RETRY_DELAY', '10'))


# Подключение к Reddit API
reddit = praw.Reddit(
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    password=reddit_password,
    user_agent=reddit_user_agent,
    username=reddit_username,
)

# Считывание списка пользователей Reddit из файла
file_path = 'reddit_users.txt'
with open(file_path, 'r') as file:
    reddit_users = [line.strip() for line in file.readlines()]


def main():
    for attempt in range(max_retries):
        try:
            with psycopg2.connect(database=db_name, user=db_user, password=db_password, host=db_host,
                                  port=db_port) as connection:
                logging.info("Connection to PostgreSQL DB successful")

                for index, username in enumerate(reddit_users, start=1):
                    logging.info(f"Processing user {index}/{len(reddit_users)}: {username}")
                    user = reddit.redditor(username)

                    update_user_info(connection, user, max_retries, retry_delay )
                    for post in user.submissions.new(limit=10):
                        add_posts(connection, post, max_retries, retry_delay)
                    for comment in user.comments.new(limit=10):
                        add_comments(connection, comment, max_retries, retry_delay)

                break

        except psycopg2.OperationalError as e:
            logging.error(f"Attempt {attempt + 1}: Could not connect to the database: {e}")
            time.sleep(retry_delay)
        except Exception as e:
            logging.error(f"Failed to process due to: {e}")
            break

    else:
        logging.error(f"All {max_retries} retries failed.")

    logging.info("Finished processing all users.")


if __name__ == "__main__":
    main()