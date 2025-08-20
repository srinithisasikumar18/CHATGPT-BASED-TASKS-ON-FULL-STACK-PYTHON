# Combination of Both
#9--Find all prime numbers between 1 and 50.
num=int(input("enter:"))
if num<=1:
    print("not prime")
else:
    for i in range(2,num):
        if num%i==0:
            print("not prime")
            break
    else:
        print("prime")