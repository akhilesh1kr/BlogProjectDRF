Blog project

Tools Used:
Django 2.2
Django Rest Framework 3.9.4
SQLite
Django Rest Auth
Django Allauth

How to use project
1. Initiate Virtual Environment
$ sudo -H pip3 install -U pipenv    # only if pipenv is not installed in system
$ pipenv --python 3.6
$ pipenv shell

2. Install Requirements
$ pip install -r requirements.txt

3. Migrate
$ python manage.py migrate

4. Runserver
$ python manage.py runserver

The Website could be run on browser at http://127.0.0.1:8000/api/v1/