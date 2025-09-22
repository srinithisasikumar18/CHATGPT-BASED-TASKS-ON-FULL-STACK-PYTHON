fp=open('numbers.txt','r')
sum=0
for i in fp:
    # print(type(i))
    print(i.strip())
    sum=int(i.strip())+sum
print(sum)
