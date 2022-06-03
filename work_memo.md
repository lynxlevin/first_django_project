First Django Project


- `django-admin startproject project_name`
- `python3 manage.py startapp app_name`
- code below files
	- app_name/urls.py
	- app_name/views.py
	- project_name/urls.py
- `python3 manage.py runserver`
- `python3 manage.py migrate`
- check for database by using `sqlite3 database_name` database_name is in settings.py (db.sqlite3)
- code below files
	- app_name/models.py
	- project_name/settings.py: add to INSTALLED APPS
- `python3 manage.py makemigrations app_name`
- check actual sql with `python3 manage.py sqlmigrate app_name 0001`
- `python3 manage.py migarate`
- try making datas via shell`python3 manage.py shell`
- add __str__ method to models.py
- `python3 manage.py createsuperuser`
- add Question to polls/admin.py

## add Client for testing view
- `python3 manage.py shell`
```
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
>>> from django.test import Client
>>> client = Client()
>>> response = client.get('/')
>>> response.status_code
>>> from django.urls import reverse
>>> response = client.get(reverse('polls:index'))
>>> response.status_code
>>> response.content
>>> response.context['latest_question_list']
```

[はじめての Django アプリ作成、その 7](https://docs.djangoproject.com/ja/4.0/intro/tutorial07/)だけやってない


今、音声ファイルのアップロード、flacへの変換、文字起こし、ファイルの削除まで実装ができました。
バリデーションはファイルサイズだけかけています。

あとしたいことは、(done)複雑な処理のモジュール化、バリデーションの改善、ユニットテストの実装、zoom連携でauthorization codeを使うこと、(done)zoom apiからミーティング履歴を取得して選べるようにすることです。

この音声ファイルは、時間の制限とかあるのだろうか？
いろいろとじっくり考えていきたいです



def convert_time(time_str):
    return datetime.datetime.strptime('2022-02-20T00:40:19Z', '%Y-%m-%dT%H:%M:%SZ')




http.client.HTTPSConnection    コンストラクタでMockConnectionを返したい

MockConnection
    def requestでself.responseをセット
	  def getresponseでself.responseを返す（これはMockResponse）


MockResponse
　　def readで{'answer': 'test_data'}を返す

それが、json.loadsされて返される



# Using Mysql

create database
`mysql`
`CREATE DATABASE gadget_collection CHARACTER SET utf8;`

change DATABASE in settings.py
add my.cnf
`python3 manage.py makemigrations`
`python3 manage.py migrate`