# API Yatube

Api для Yatube.
Сервис для публикации своих постов, комментариев.

## Возможности

- Просмотр, создание, изменение и удаление записей.
- Возможность добавления, редактирования, удаления своих комментариев и просмотр чужих.
- Просмотр и создание групп.
- Подписки на пользователей.
- Фильтрация по полям.
- Для аутентификации используются JWT-токены.

## Технологии

Для создания были использованы:
- [Python 3.9.0](https://www.python.org)
- [Django 3.2.16](https://www.djangoproject.com)
- [djangorestframework 3.12.4](https://www.django-rest-framework.org)
- [JWT + Djoser](https://djoser.readthedocs.io/en/latest/index.html)

## Установка

- Клонируйте(скачайте) данный репозиторий


Установите виртуальное окружение:
```sh
$python -m venv venv
```

Запустите виртуальное окружение:
```sh
$source venv/scripts/activate
```

Установите зависимости из requirements.txt:
```sh
$pip install -r reqiurements.txt
```

Выполните миграции:
```sh
$cd yatube_api
$python manage.py migrate
```

Запустите сервер:
```sh
$python manage.py runserver
```

Api доступен по адресу http://127.0.0.1:8000/api/v1/

## Документация

Вся документация доступна по ссылке: http://127.0.0.1:8000/redoc/
