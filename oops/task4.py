class Employee:
    company_name="TechCorp"
    def __init__(self,ename,eid):
        self.name=ename
        self.id=eid
    def display(self):
        print("Name",self.name)
        print("id",self.id)
        print("company name",Employee.company_name)
        print('-----------------------------')
e1=Employee("srinithi",101)
e2=Employee("karthik",102)
e1.display()
e2.display()
Employee.company_name="HCL"
e1.display()
e2.display()