# LEVEL--1
# 1--------------------------------------------------------------------
fruit=["banana","apple","grape","stawberry","mango"]
for i in fruit:
    print(i)
#2--------------------------------------------------------------------
numbers_su=(1,2,3,4)
result=sum(numbers_su)
print(result)
s=0
for i in numbers_su:
    s=s+i
print(s)
#3--------------------------------------------------------------------
colors = ["red", "green", "blue", "yellow"]
print(colors[1])
print(colors[3])
# ====================================================================
# LEVEL-2
# 1--------------------------------------------------------------------
numbers = [1, 2, 3, 4, 5]
numbers[3]=99
print(numbers)
#2--------------------------------------------------------------------
fruit=["banana","apple","grape","stawberry"]
fruit.append("mango")
fruit1=["pineapple", "grape"]
fruit.extend(fruit1)
print(fruit)
#3--------------------------------------------------------------------
person = ("John", 25, "Engineer")
name,age,profession=person
print(f"{name} is a {age}-year-old { profession}")
# ====================================================================
# LEVEL-3
# 1--------------------------------------------------------------------
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[1:5])
#2--------------------------------------------------------------------
fruit=["banana","apple","grape","stawberry"]
k="banana" in fruit
if "banana" in fruit:
    print("yes")
else:
    print("No")
print("True")
# 3--------------------------------------------------------------------
m=[2, 4, 2, 6, 2, 8]
print(m.count(2))
# =====================================================================
# LEVEL_4
shopping_cart=["milk", "bread", "eggs"]
item1=input("enter the item1 into your cart").lower()
item2=input("enter the item2 into your cart").lower()
shopping_cart.append(item1)
shopping_cart.append(item2)
print(shopping_cart)
shopping_cart=tuple(shopping_cart)
print(shopping_cart)