#2-Find the smallest of three numbers.
num1=int(input("Enetr the first Number"))
num2=int(input("Enetr the second number"))
num3=int(input("Enetr the third NUmber"))
if num1<num2 and num1<num3:
    print("num1 is smallest")
elif num2<num1 and num2<num3:
    print("num2 is smallest")
else:
    print("num3 is smallest")