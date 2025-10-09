import mysql.connector
dbcon=mysql.connector.connect(host='localhost',
                              user='root',
                              password='#Srinithi4877',
                              database='testdb')
cursor=dbcon.cursor()
sql_st='''
create table if not exists employees
(
eid int PRIMARY KEY,
ename varchar(32),
esal float
)
'''
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
cursor.execute(sql_st)
cursor.executemany(sql_insert,values)
cursor.execute("select * from employees")
rows=cursor.fetchall()
print(rows)
print("table creates and values insertes")
cursor.close()
dbcon.close()