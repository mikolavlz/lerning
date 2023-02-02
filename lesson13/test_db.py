import pymysql.cursors
from pymysql import *

connect = connect(host='localhost',user='root',password='',db='Lesson12',cursorclass=pymysql.cursors.DictCursor)

with connect:
   cur =  connect.cursor()
   title = input('Введите марку авто ')
   price = int(input(f'Введите стоимость{title}'))

   sql_update = f' insert into goods (price, title) values( "{price}" ,"{title}")'
   cur.execute(sql_update)
   cur.execute('select * from goods')
   rows = cur.fetchall()
   # print(rows)
   for item in rows:
       print(f'Автомобиль{item["title"]} стоит {item["price"]}')
   connect.commit()