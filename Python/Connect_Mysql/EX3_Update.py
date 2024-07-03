import pymysql
import sys
#id = int(input("Enter actor id :"))
#col_name = input("Enter column name :")
#value = input("Enter Rename Value :")
conn = pymysql.connect(host='localhost',user='root',password='rps@123',db='sakila')

if not conn:
    sys.exit(0)
try:
    cur = conn.cursor()
   # cur.execute(f"update actor set {col_name}={value} where actor_id={id}")
    cur.execute("update actor set first_name='SIVA' where actor_id=201")
    conn.commit()
except pymysql.Error as e:
    print(e)
else:
    print("Record Updated")
finally:
    conn.close()