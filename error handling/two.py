try:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
except ValueError as err:
    print(err)
    print(" have entered a string instead of NUmber")