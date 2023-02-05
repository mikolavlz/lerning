import pymysql.cursors
from pymysql import *

connect = connect(host='localhost',user='root',password='',db='Lesson12',cursorclass=pymysql.cursors.DictCursor)
with connect:
   cur =  connect.cursor()
   cur.execute('select * from student')
   rows = cur.fetchall()
   # print(rows)
   for item in rows:
       print(f'У студента {item["name"]} средний бал =  {item["ball"]}')
   # print(rows)
