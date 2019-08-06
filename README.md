#### demo1: Python and Postgres Tutorial with psycopg2
01. Check psycopg2

```bash
➜   python
Python 2.7.10 (default, Oct  6 2017, 22:29:07)
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import psycopg2
```

02. Init a postgres database: **db_demo_1**

Set up postgres

```bash
$ docker run --name flask-postgres-demo \
-e POSTGRES_PASSWORD=123456 \
-p 5432:5432 \
-d postgres:9.6.10-alpine
```

```bash
➜  flask-postgres-demo git:(master) ✗ docker exec -it flask-postgres-demo bash
bash-4.4# psql -U postgres
psql (9.6.10)
Type "help" for help.

postgres=# create database flask_demo
```


```bash
postgres=# create database db_demo_1;
CREATE DATABASE
postgres=# \c db_demo_1;
You are now connected to database "db_demo_1" as user "postgres".
```

create a table: **users**
```bash
CREATE TABLE USERS(
   user_id serial PRIMARY KEY,
   username VARCHAR (50) UNIQUE NOT NULL,
   age integer  UNIQUE NOT NULL,
   address VARCHAR (255) 
);
```

03. Insert data to table 

```bash
INSERT INTO USERS(  user_id, username, age, address)  
VALUES
(1, 'Maxsu', 25, '海口市人民大道2880号'), 
(2, 'minsu', 20, '北京市朝阳区' ), 
(3, 'Larry', 21, '武汉保利大厦');
```

```bash
db_demo_1=# select * from users;                                      user_id | username | age |       address
---------+----------+-----+----------------------
       1 | Maxsu    |  25 | 海口市人民大道2880号
       2 | minsu    |  20 | 北京市朝阳区
       3 | Larry    |  21 | 武汉保利大厦
(3 rows)
```

04. Run python with python 2.7.x or python 3

`python 01_postgres_demo.py` or `python3 01_postgres_demo.py`

Get result from the console:
```bash
➜  python-demo git:(master) ✗ python3 01_postgres_demo.py
我是中文
user_id -> 1 user_name -> Maxsu address -> 海口市人民大道2880号
user_id -> 2 user_name -> minsu address -> 北京市朝阳区
user_id -> 3 user_name -> Larry address -> 武汉保利大厦
```
---