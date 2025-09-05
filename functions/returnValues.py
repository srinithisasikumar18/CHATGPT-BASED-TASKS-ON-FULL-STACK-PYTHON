
# def factorial(n):
#     if n==0 or n--1:
#         return 1
#     else:
#         return n*factorial(n-1)
# n=int(input("enter"))
# print(factorial(n))



nums=int(input("enter the no of elemnts in list:"))
old=[]
new=[]
def square_list(nums):
    for i in range(nums):
        elements=int(input("enter the number:"))
        old.append(elements)
        new.append(elements*elements)
    return old,new   
print(square_list(nums))