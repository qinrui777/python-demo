# encoding: utf-8
import psycopg2

# please have a look at README.md 
# demo1: Python and Postgres Tutorial with psycopg2

#connect to the db, ref:http://initd.org/psycopg/docs/module.html
con = psycopg2.connect(
    host = '127.0.0.1',
    database = 'db_demo_1',
    user = 'postgres',
    password = '123456',
    port = 5432
)

#cursor
cur = con.cursor()

#data is exist, execute query
cur.execute("select * from users")

rows = cur.fetchall()
print ("我是中文")

for r in rows:
    # python 3
    # print (f"user_id {r[0]}")

    # python 2
    print r[0],r[1],r[2],r[3]

#commit the transcation
con.commit()

#close the cursor
cur.close()

#close the connection
cur.close()
