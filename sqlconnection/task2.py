import mysql.connector
dbcon=mysql.connector.connect(host='localhost',
                              user='root',
                              password='#Srinithi4877',
                              database='task2')
cursor=dbcon.cursor(dictionary=True)
# sql_st='''
# create database if not exists task2;
# '''
sql_table='''
create table if not exists employee
(
eid int primary key,
ename varchar(32),
esal float
)
'''
# cursor.execute(sql_st)
cursor.execute(sql_table)
print("database is created, name of the database 'task2")
print("A table with id, name, sal is created")
while True:
    print("Select the following user inputs:")
    print("1.Add Employees")
    print("2.View Employees")
    print("3.Update Employees")
    print("4.Exit")
    Choice=int(input("Enter Choice:"))
    if Choice==1:
        eid=int(input("Enter the eid:"))
        cursor.execute("select * from employee WHERE eid=%s",(eid,))
        record=cursor.fetchone()
        if record:
            print("already exists")
        else:
            ename=input("Enter the name:")
            esal=int(input("Enter the Salary:"))
            cursor.execute("insert into employee (eid,ename,esal) " 
            "values (%s,%s,%s)",(eid,ename,esal))
            dbcon.commit()
            print("Record created")
    elif Choice==2:
            cursor.execute("select * from employee")
            rows=cursor.fetchall()
            if not rows:
                 print("No record was found")
            else:
                for row in rows:
                    print(f"eid:{row['eid']},ename:{row['ename']},esal:{row['esal']}")
    elif Choice==3:
         while True:
              print("1.id")
              print("2.name")
              print("3.sal")
              print("4.Exit")
            
              Choose=int(input("which field you want to update"))
              if Choose==1:
                   old_eid=int(input("enter eid you want to change"))
                   new_eid=int(input("enter new id:"))
                   cursor.execute("update employee set eid=%s where eid=%s",(new_eid,old_eid))
                   dbcon.commit()
                   print("Eid updated")
              elif Choose==2:
                   eid=int(input("Enter the eid:"))
                   cursor.execute("select * from employee where  eid=%s",(eid,))
                   record=cursor.fetchall()
                   if not record:
                        print("eid not there in the record")
                   else:
                        new_name=input("enter the new name")
                        cursor.execute("update employee set ename=%s where eid=%s",(new_name,eid))
                        dbcon.commit()
                        print("Name updated at",record)
              elif Choose == 3:
                while True:
                    print("1. Update salary using EID")
                    print("2. Update salary using Name")
                    print("3. Exit")
                    update_with = int(input("Enter your option: "))

                    if update_with == 1:
                        eid = int(input("Enter the EID: "))
                        cursor.execute("SELECT * FROM employee WHERE eid=%s", (eid,))
                        record = cursor.fetchone()
                        if not record:
                            print("Employee ID not found.")
                        else:
                            new_esal = float(input("Enter the new salary: "))
                            cursor.execute("UPDATE employee SET esal=%s WHERE eid=%s", (new_esal, eid))
                            dbcon.commit()
                            print("Salary updated successfully!")

                    elif update_with == 2:
                        ename = input("Enter the employee name: ")
                        cursor.execute("SELECT * FROM employee WHERE ename=%s", (ename,))
                        record = cursor.fetchone()
                        if not record:
                            print("Employee name not found.")
                        else:
                            new_esal = float(input("Enter the new salary: "))
                            cursor.execute("UPDATE employee SET esal=%s WHERE ename=%s", (new_esal, ename))
                            dbcon.commit()
                            print("Salary updated successfully!")
                    elif update_with == 3:
                        print("Exiting salary update menu.")
                    else:
                        print("Invalid choice. Please try again.")
                        break

       


    else :
        print("Invalid Choice")
        break
cursor.close()
dbcon.close()