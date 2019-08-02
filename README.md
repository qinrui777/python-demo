##### demo1: Python and Postgres Tutorial with psycopg2
check psycopg2

```bash
➜   python
Python 2.7.10 (default, Oct  6 2017, 22:29:07)
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import psycopg2
```

init a postgres database: **db_demo_1**

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

insert data to table 

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

run python with python 2.7.x
`python 01_postgres_demo.py`

get result from the console:
```bash
➜  python-demo git:(master) python 01_postgres_demo.py
我是中文
1 Maxsu 25 海口市人民大道2880号
2 minsu 20 北京市朝阳区
3 Larry 21 武汉保利大厦
```

---