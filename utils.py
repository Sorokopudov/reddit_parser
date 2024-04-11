import time
import logging
from datetime import datetime


def update_user_info(connection, user, max_retries, retry_delay):
    attempt = 0
    while attempt < max_retries:
        try:
            with connection.cursor() as cursor:
                query = """
                INSERT INTO users (id, username, link_karma, post_karma, created_at)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (id) DO UPDATE
                SET link_karma = EXCLUDED.link_karma,
                    post_karma = EXCLUDED.post_karma;
                """
                cursor.execute(query, (str(user.id), user.name, user.link_karma, user.comment_karma, datetime.now()))
                connection.commit()
            logging.info(f"Updated user info for {user.name}")
            break
        except Exception as e:
            logging.error(f"Attempt {attempt + 1}: Error updating user info for {user.name}: {e}")
            attempt += 1
            if attempt < max_retries:
                logging.info(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                logging.error(f"Failed to update user info for {user.name} after {max_retries} attempts.")

def add_posts(connection, post, max_retries, retry_delay):
    attempt = 0
    while attempt < max_retries:
        try:
            with connection.cursor() as cursor:
                query = """
                INSERT INTO posts (id, title, text, subreddit_id, user_id, created_at)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING;
                """
                cursor.execute(query, (post.id, post.title, post.selftext, post.subreddit_id, post.author.id, datetime.now()))
                connection.commit()
                if cursor.rowcount > 0:  # Проверка, была ли добавлена строка
                    logging.info(f"Added new post {post.id} for user {post.author}")
                # else:
                #     logging.info(f"Post {post.id} already exists, not added.")
                break
        except Exception as e:
            logging.error(f"Attempt {attempt + 1}: Error adding post {post.id} for user {post.author}: {e}")
            attempt += 1
            if attempt < max_retries:
                logging.info(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                logging.error(f"Failed to add post {post.id} for user {post.author} after {max_retries} attempts.")


def add_comments(connection, comment, max_retries, retry_delay):
    attempt = 0
    while attempt < max_retries:
        try:
            with connection.cursor() as cursor:
                query = """
                INSERT INTO comments (id, text, parent_id, subreddit_id, user_id, created_at)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING;
                """
                cursor.execute(query, (comment.id, comment.body, comment.parent_id, comment.subreddit_id, comment.author.id, datetime.now()))
                connection.commit()
                if cursor.rowcount > 0:  # Проверка, была ли добавлена строка
                    logging.info(f"Added new comment {comment.id} for user {comment.author}")
                # else:
                    # logging.info(f"Comment {comment.id} already exists, not added.")
                break
        except Exception as e:
            logging.error(f"Attempt {attempt + 1}: Error adding comment {comment.id} for user {comment.author}: {e}")
            attempt += 1
            if attempt < max_retries:
                logging.info(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                logging.error(f"Failed to add comment {comment.id} for user {comment.author} after {max_retries} attempts.")
