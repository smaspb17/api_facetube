# API Final Yatube
**ОПИСАНИЕ:**

API Yatube - это приложение, разрабатанное с использованием Django REST framework для реализации API. Проект включает в себя компоненты, необходимые для предоставления API-сервисов, такие как маршрутизация URL, сериализаторы, модели, представления, аутентификация, управление доступом. DRF  обеспечивает поддержку для формата зaпросов JSON.

**ЛОКАЛЬНАЯ УСТАНОВКА:**

1. Установить Python на компьютер, если он еще не установлен. Версия Python должна быть не ниже 3.6.

2. Создать виртуальное окружение для проекта. Это позволит изолировать проект от системных зависимостей и установленных библиотек. Для создания виртуального окружения используется команда:
```
python3 -m venv myenv
```

3. Активировать виртуальное окружение командой:
```
source myenv/bin/activate
```

4. Установить необходимые пакеты и зависимости проекта через менеджер пакетов `pip` и `requirements.txt` файл. Он должен содержать в себе список всех зависимостей, необходимых для работы проекта:
```
pip install -r requirements.txt
```

5. Установить Django Rest Framework через pip:
```
pip install djangorestframework
```

6. Создать Django проект командой:
```
django-admin startproject myproject
```

7. Создать Django приложение командой:
```
python manage.py startapp myapp
```

8. Настроить базу данных в настройках проекта в файле settings.py. Например, можно использовать SQLite в качестве БД:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

9. Создать модели для работы с данными в БД. Пример:
```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_at = models.DateField()
```

10. Создать сериализаторы (Serializers) для преобразования объектов моделей в форматы JSON (или другой, например XML) и наоборот. Пример:
```python
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
```

11. Создать Views для обработки запросов и возврата ответов в нужном формате. Пример:
```python
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer
```

12. Зарегистрировать URLs приложения для обработки запросов. Пример:
```python
from django.urls import include, path
from rest_framework import routers
from .views import BookViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
```

После этих действий, API проект должен быть готов к запуску на локальном компьютере. Запуск проекта осуществляется командой:
```
python manage.py runserver
```

**АВТОР:** Марат


**ЛИЦЕНЗИЯ:** То ли еще будет


**КОНТАКТЫ:** smaspb17@yandex.ru
