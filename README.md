# Quiz Backend API

Небольшой backend для платформы с викторинами.
Проект написан на FastAPI с использованием PostgreSQL, Redis и Docker.

## Что используется в проекте

* FastAPI
* PostgreSQL
* Redis
* SQLAlchemy
* Docker
* JWT авторизация
* Pytest

## Запуск проекта

```bash
docker compose up --build
```

## Swagger документация

После запуска проекта документация будет доступна по адресу:

```txt
http://localhost:8000/docs
```

## Возможности проекта

* Регистрация и авторизация пользователей
* JWT аутентификация
* Работа с вопросами (CRUD)
* API для игр
* API для ответов
* Поддержка Redis Pub/Sub
