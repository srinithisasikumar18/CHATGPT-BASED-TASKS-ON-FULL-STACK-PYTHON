#1
import math
print(math.sqrt(225))
print(math.pi)
print(math.e)
print(math.factorial(6))
print(math.ceil(5.9))
print(math.floor(5.9))

#2
import random
print(random.randint(1,50))
print(random.uniform(0,1))
fruits=["Mango","Strawbeery","grape","banana","apple"]
print(random.choice(fruits))
num=[1,2,3,4,5]
print(random.shuffle(num))
print(num)

#3
import datetime
# print(datetime.datetime.today())#--today's date and time
# print(datetime.datetime.now().time())
# print(datetime.datetime.now().today())
print(datetime.date.today())#-today's date only
today=datetime.date.today()
print("Year:", today.year)
print("Month",today.month)
print("Day:",today.day)
print("Current Time:",datetime.datetime.now().time())
birthday=datetime.datetime(2003,1,9,10,30,1)
print("My Birthday:",birthday)

#4




