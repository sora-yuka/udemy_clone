# Клон Udemy на Django Rest Framework

### Это онлайн платформа для публикации и покупки разных курсов.
---
#### Доступный функционал на данный момент:

  - Регистрация и авторизация через почту.
  - Сброс пароля через почту.
  - Просмотр профиля.
  - Загрузка курсов на платформу.
  - Покупка курсов.
  - Возможность оставить комментарии и поставить рейтинг.
  - Возможность поставить лайки на комментарии.

---

### Использованные библиотеки:

![Flutter](https://img.shields.io/badge/-Django-yellow?style=for-the-badge&logo=python) 

![Flutter](https://img.shields.io/badge/-Django_Rest-yellow?style=for-the-badge&logo=python)

![Flutter](https://img.shields.io/badge/-Simple_JWT-yellow?style=for-the-badge&logo=python)

![Flutter](https://img.shields.io/badge/-psycopg2_binary-yellow?style=for-the-badge&logo=python)

![Flutter](https://img.shields.io/badge/-django_filter-yellow?style=for-the-badge&logo=python)

![Flutter](https://img.shields.io/badge/-drf_yasg-yellow?style=for-the-badge&logo=python)

![Flutter](https://img.shields.io/badge/-celery_[redis]-yellow?style=for-the-badge&logo=python)

![Flutter](https://img.shields.io/badge/-pillow-yellow?style=for-the-badge&logo=python)

---

#### Для хранения данных использовалась база данных PostgreSql

---

### Чтобы запустить проект, необходимо:

  - Скопировать репозиторий.
    ```
    git clone https://github.com/sora-yuka/udemy_clone.git
    ```

  - Создать и активировать виртуальное окружение.  
    ```virtualenv venv``` или ```python -m venv venv```


  - Установить все необходимые зависимости.
    ```
    pip install -r requirements.txt
    ``` 

  - Настроить файл ".env"
 
  - Сделать миграцию.
    ```
    ./manage.py makemigrations
    ./manage.py migrate
    ``` 

  - Запустить проект.
    ```
    ./manage.py runserver
    ``` 