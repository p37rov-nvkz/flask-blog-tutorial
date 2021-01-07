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

#Создание таблицы

1. import models
2. from app import db
3. db.create_all()


#Запуск приложения

pip install -r requirements.txt
python main.py
