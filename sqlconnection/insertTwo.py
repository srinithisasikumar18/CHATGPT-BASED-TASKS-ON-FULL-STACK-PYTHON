import mysql.connector
dbcon=mysql.connector.connect(host='localhost',
                              user='root',
                              password='#Srinithi4877',
                              database='testdb')
cursor=dbcon.cursor()
sql_insert='''
insert into employees(eid,ename,esal)
values (%s,%s,%s);
'''
values=[
(101,'kokila',50000),
(102,'sasi',60000),
(103,'kamal',80000)
]
dbcon.commit()
cursor.executemany(sql_insert,values)
dbcon.commit()
print("table creates and values insertes")  