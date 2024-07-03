import pymysql
import sys

conn = pymysql.connect(host='localhost',user='root',password='rps@123',db='sakila')

if not conn:
    sys.exit(0)
try:
    cur = conn.cursor()
    cur.execute("insert into actor values(201, 'SIVA','BALAN',CURRENT_TIMESTAMP)")
    conn.commit()
except pymysql.Error as e:
    print(e)
else:
    print("Record Inserted")
finally:
    conn.close()