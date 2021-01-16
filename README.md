# flask-blog-tutorial
Flask Blog Using CSS Bootstrap

#Установка MySQL 

https://www.digitalocean.com/community/tutorials/mysql-ubuntu-18-04-ru

#Создание базы данных для проекта

create database flask_blog_tutorial_db character set utf8 collate utf8_unicode_ci;

#Определить переменные окружения:
DB_USER, DB_PASSWORD, DB_NAME

1. Создать файл: ./venv/lib/python3.8/site-packages/_set_envs.pth
2. Записать в файл: import os; os.environ['FOO'] = 'bar'

#Создание таблиц
1. from app import app
2. import models
3. from app import db
4. db.create_all()

#Выполнение миграций
    #Первоначальная инициализация
        1. python manage.py db init
    #Создание миграции
        1. python manage.py db migrate
    #Выполнение миграции
        1. python manage.py db upgrade

#Создание пользователя
1. from app import db
2. from app import user_datastore
3. user_datastore.create_user(email='email', password='password')
4. db.session.commit()

#Создание роли
1. from app import db
2. from models import User, Role
3. from app import user_datastore
4. user = User.query.first()
5. user.email
'p37rov.nvkz@gmail.com'
6. user_datastore.create_role(name='admin', description='administrator')
<Role (transient 139985834980736)>
7. db.session.commit()
8.role = Role.query.first()
9. user_datastore.add_role_to_user(user, role)
True
10. db.session.commit()
#Запуск приложения

pip install -r requirements.txt
python main.py
