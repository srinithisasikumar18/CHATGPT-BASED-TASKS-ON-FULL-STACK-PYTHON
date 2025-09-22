list=[]
a=int(input("enter  the no of elements in  list"))
for i in range(a):
    b=int(input("enter the numbers in list"))
    list.append(b)
print(list)
try:
    index=int(input("enter the index "))
    print(list[index])
except IndexError as err:
    print(err)
