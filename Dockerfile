# Базовый образ Python 
FROM python:3.9-slim

# Рабочая директория
WORKDIR /app

# Файлы в контейнер
COPY main.py utils.py reddit_users.txt /app/

# Зависимости
RUN pip install psycopg2-binary praw python-dotenv

# Скрипт при запуске контейнера
CMD ["python", "main.py"]
