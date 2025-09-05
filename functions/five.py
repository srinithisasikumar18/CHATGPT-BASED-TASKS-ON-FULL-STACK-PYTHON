def total(*numbers):
    sum=0
    for i in numbers:
        sum=i+sum
    return sum
print(total(1,2,3,4))
print(total(2,34))


def print_details(**info):
    for i in info:
        print(i,":",info[i])
print_details(name="srinithi",age=22,city="bengaluru")




