import pymysql
import sys

conn = pymysql.connect(host='localhost',user='root',password='rps@123',db='sakila')

if not conn:
    sys.exit(0)
try:
    cur = conn.cursor()
except pymysql.Error as e:
    print(e)
else:
    try:
        cur.execute("select actor_id, first_name from actor")
    except pymysql.Error as e:
        print(e)
    else:
        records = cur.fetchall()
        for rec in records:
            print(f"Number:{rec[0]},FName:{rec[1]}")
finally:
    conn.close()