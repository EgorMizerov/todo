# todo

## Установка
```
git clone https://github.com/EgorMizerov/todo.git
```
### Windows
1. Скачать Python
https://www.python.org/downloads/
2. Установить необходимые пакеты:
  ```python -m pip install --upgrade pip
  pip install django
  pip install psycopg2
  ```
3. Скачать PostgreSQL
https://postgrespro.ru/windows
4. Настройка базы данных
  ```
  cd c:\Program Files\PostgreSQL\13\bin
  psql postgres
  
  create user usertest with password 'Pass123';
  alter role usertest set client_encoding to 'utf8';
  alter role usertest set default_transaction_isolation to 'read committed';
  alter role usertest set timezone to 'UTC';
  
  create database test_db owner usertest;
```
5. Установить миграцию и создать суперпользователя
```
  python manage.py migrate
  python manage.py createsuperuser
```
6. Запуск проекта
```
  python manage.py runserver
```

### Linux(Debian-подобные)
1. Скачать PostgreSQL
```
sudo apt-get install postgresql postgresql-contrib
```
2. Установка необходимых пакетов
  ```
  python3 -m pip install --upgrade pip
  sudo apt-get install libpq-dev python-dev
  pip3 install django
  pip3 install psycopg2
  ```
3. Настройка базы данных
  ```
  psql postgres
  
  create user usertest with password 'Pass123';
  alter role usertest set client_encoding to 'utf8';
  alter role usertest set default_transaction_isolation to 'read committed';
  alter role usertest set timezone to 'UTC';
  
  create database test_db owner usertest;
```
4. Установить миграцию и создать суперпользователя
```
  python manage.py migrate
  python manage.py createsuperuser
```
5. Запуск проекта
```
  python manage.py runserver
```
