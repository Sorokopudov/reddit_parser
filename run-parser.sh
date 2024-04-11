#!/bin/bash

# Проверка что база данных запущена
docker-compose up -d db

# Запуск парсера
docker-compose up --no-deps --build -d reddit-parser
