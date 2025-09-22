a=int(input("enter the first number"))
b=int(input("enter the second number"))
try:
    print(a/b)
except ZeroDivisionError as err:
    print(err)
    print("Cannot divide by zero")
