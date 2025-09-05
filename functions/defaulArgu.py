def greet_user(name="Guest"):
    if name=="":
        return "Hello, Guest"
    else:
        print ("Hello,",name)
name=input("enter the name:")
print(greet_user(name))