def greet():
    print("Hello, Welcome to Python!")
greet()

def add(a,b):
    return a+b
print(add(5,7))

def is_even(num):
    if num%2==0:
        return True
    else:
        return False
num=int(input("enter the number:"))
print(is_even(num))