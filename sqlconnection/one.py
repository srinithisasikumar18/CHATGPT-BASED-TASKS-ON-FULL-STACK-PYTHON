import mysql.connector
dbcon=mysql.connector.connect(host='localhost',
                              user='root',
                              password='#Srinithi4877')
cursor=dbcon.cursor()
cursor.execute("CREATE DATABASE if not exists testdb")

print("Database Created")

dbcon.commit()
cursor.close()
dbcon.close()


