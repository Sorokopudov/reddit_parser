# Reddit Parser Docker Project

## Описание

Этот проект предназначен для парсинга данных пользователей Reddit и сохранения их в базу данных PostgreSQL. Проект включает в себя скрипт парсера, написанный на Python, который использует API Reddit для получения данных, а также Docker-контейнеры для запуска парсера и базы данных.

## Структура проекта

- `main.py`: Основной скрипт парсера.
- `utils.py`: Вспомогательные функции для `main.py`.
- `Dockerfile`: Файл для создания Docker-образа парсера.
- `docker-compose.yml`: Конфигурация Docker Compose для запуска сервисов.
- `init.sql`: SQL-скрипт для инициализации структуры базы данных.
- `.env`: Файл с переменными окружения для конфигурации проекта.
- `reddit_users.txt`: Список пользователей Reddit для парсинга.
- `run.sh`: Bash-скрипт для запуска всех сервисов.
- `run-parser.sh`: Bash-скрипт для повторного запуска только парсера.

## Как использовать

### Настройка

Перед запуском убедитесь, что у вас установлен Docker и Docker Compose. Клонируйте репозиторий и создайте файл `.env` с вашими конфигурациями.

### Запуск

Чтобы запустить все сервисы, выполните:

```bash
./run.sh

Для повторного запуска только парсера используйте:

```bash
./run-parser.sh

### Конфигурация

Для настройки проекта измените файл .env, указав требуемые переменные окружения:

    - DB_NAME: имя базы данных.
    - DB_USER: имя пользователя для доступа к базе данных.
    - DB_PASSWORD: пароль пользователя.
    - DB_PORT: порт для подключения к базе данных.
    - REDDIT_CLIENT_ID: ваш ID клиента для Reddit API.
    - REDDIT_CLIENT_SECRET: ваш секрет клиента для Reddit API.
    - REDDIT_PASSWORD: ваш пароль для Reddit.
    - REDDIT_USER_AGENT: user agent для вашего скрипта Reddit API.
    - REDDIT_USERNAME: ваше имя пользователя на Reddit.
    - MAX_RETRIES: максимальное количество попыток для переподключения или запросов.
    - RETRY_DELAY: время задержки между попытками в секундах.

## Пример файла .env :

# Database credentials
DB_NAME=reddit_user_activity_docker
DB_USER=postgres
DB_PASSWORD=aaaaa123456
DB_PORT=5432


# Reddit API credentials
REDDIT_CLIENT_ID=W..........A
REDDIT_CLIENT_SECRET=W................A
REDDIT_PASSWORD=R...........8
REDDIT_USER_AGENT=testscript by u/User_82
REDDIT_USERNAME=User_82

MAX_RETRIES=5  
RETRY_DELAY=10 

