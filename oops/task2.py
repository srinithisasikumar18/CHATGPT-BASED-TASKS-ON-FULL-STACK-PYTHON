class School:
    School_name="MBU"
    def __init__(self,id,name):
        self.id=id
        self.name=name
        
s1=School(1,"srinithi")
print("before")
print(s1.__dict__)
School.School_name="SDHR"
print("after changing")
print(s1.__dict__)
s2=School(2,"kokila")
print(s1.School_name)
print(s2.School_name)

print(s2.__dict__)