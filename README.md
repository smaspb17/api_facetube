# API Facetube
## ОПИСАНИЕ:

API Facetube - это приложение, разрабатанное с использованием Django REST framework, для реализации API того же функционала, что и в проекте Facetube (https://github.com/smaspb17/facetube) - соцсети по созданию постов. Проект включает в себя компоненты, необходимые для предоставления API-сервисов, такие как маршрутизация URL, сериализаторы, модели, представления, аутентификация, управление доступом. DRF обеспечивает поддержку формата зaпросов JSON.

В проекте реализовано создание/обновление/удаление по HTTP-запросам постов пользователя, подписок, отзывов и комментариев на посты, в базе данных SQLite3.Также возможны запросы на создание, обновление и проверку JWT - токенов. Подробная информация отражена в документации redoc, куда можно пройти выполнив инструкцию ниже.
 
## СТЕК ТЕХНОЛОГИЙ:
Python 3.9.10, Django Rest Framework 3.14.0, SQLite3, djoser, redoc

## ЛОКАЛЬНАЯ УСТАНОВКА (для Windows):

1. Клонируй проект на свой компьютер:
```
git clone git@github.com:smaspb17/api_facetube.git
```
2. Перейди в директорию api_facetube:
```
cd api_facetube/
```
3. Создай виртуальное окружение для проекта. Это позволит изолировать проект от системных зависимостей и установленных библиотек. Для создания виртуального окружения используй команду. Требуемая версия python - 3.9.10:
```
python -m venv venv
```
4. Активируй виртуальное окружение командой:
```
source venv/Scripts/activate
```
5. Установи необходимые пакеты и зависимости проекта через менеджер пакетов `pip` и `requirements.txt` файл. Он должен содержать в себе список всех зависимостей, необходимых для работы проекта:
```
pip install -r requirements.txt
```
6. При необходимости обнови пакетный менеджер pip:
``` 
python.exe -m pip install --upgrade pip
```
7. Перейди в директорию surveys, там находится файл manage.py:
```cmd
cd yatube_api/
```
8. Выполни миграции:
```cmd
python manage.py migrate
```
9. Создай суперпользователя:
```cmd
python manage.py createsuperuser
```
10. Запусти проект на локальном сервере:
```
python manage.py runserver
```
11. Перейди по ссылке в документацию API redoc:
```
http://127.0.0.1:8000/redoc/
```
Теперь ты можешь использовать проект на своём компьютере. Если ты хочешь остановить проект, нажми Ctrl+C в терминале, а затем деактивируй виртуальное окружение командой:
```cmd
deactivate
```

## АВТОР:

Шайбаков Марат

## ЛИЦЕНЗИЯ:

нет

## КОНТАКТЫ:

smaspb17@yandex.ru
