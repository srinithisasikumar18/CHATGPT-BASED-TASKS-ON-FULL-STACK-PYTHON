name=input("enter the name:")
subject=int(input("enter the no of subjects"))
def student_report(name, *marks):
    total_marks=0
    for i in range(subject):
        sub_marks=int(input("enter the number:"))
        total_marks+=sub_marks
    print(total_marks)
    average_marks=total_marks/subject
    return average_marks
print(name,"scored an average of ",student_report(name))
