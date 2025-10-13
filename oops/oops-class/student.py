class Student:
    
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def total_marks(self):
        s=0
        for i in self.marks:
            s=i+s
        return s
    def average(self):
        average=self.total_marks()/len(self.marks)
        return average
    def grade(self):
        if self.average()>=90.0:
            print(f"{self.name}'s grade is A")
        elif self.average()>=80.0:
            print(f"{self.name}'s grade is B")
        else:
            print(f"{self.name}'s grade is C")
student1 = Student("Alice", 101, [85, 92, 78])
student2=Student("Srinithi",102,[70,80,100])
print(f"{student1.name}'s average marks is {student1.average()}")
print(f"{student2.name}'s average marks is {student2.average()}")
student1.total_marks()
student1.average()
student1.grade()
student2.total_marks()
student2.average()
student2.grade()