#1
x=10
print("Integer Type",type(x))
y=10.5
print("Float Type",type(y))
z=2+8j
print("Complex Type",type(z))

#2
Fruit=["Mango","Banana","Apple","Grape","Stawberry"]
Fruit[2]="Avacado"
print(Fruit)
      
#3
person=("srinithi","18","Bengaluru")
name,age,city=person
print(f"My name is {name},I am {age} years old, and I live in {city}")

#4
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1|set2)
print(set1.union(set2))
print(set1&set2)
print(set1.intersection(set2))

#5
student = {
    "name": "Alice",
    "age": 20,
    "course": "Python"
}
print(student["name"])
student["age"]=21
student["grade"]="A"
print(student)