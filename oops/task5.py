class Product:
    def __init__(self,id,name):
        local_var="flipkart"
        self.pro_id=id
        self.pro_name=name
        print("inside accessing")
        print("local variable",local_var)
        print("instance variable",id)
        print("instance variable", name)
        print("--------------------------------------")

p1=Product(101,"mp1")
p2=Product(102,"mp3")


print("outside accessing")
print("instance variable",p1.pro_id,p1.pro_name)
print("instance variable",p2.pro_id,p2.pro_name)

# Trying to access local_var outside will fail
# print(p1.local_var)  # ❌ Error