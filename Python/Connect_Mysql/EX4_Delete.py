import pymysql
import sys
#id = int(input("Enter actor id to Delete:"))

conn = pymysql.connect(host='localhost',user='root',password='rps@123',db='sakila')

if not conn:
    sys.exit(0)
try:
    cur = conn.cursor()
    cur.execute("delete from actor where actor_id=201")
    #cur.execute(f"delete from actor where actor_id={id}")
    conn.commit()
except pymysql.Error as e:
    print(e)
else:
    print("Record Deleted")
finally:
    conn.close()