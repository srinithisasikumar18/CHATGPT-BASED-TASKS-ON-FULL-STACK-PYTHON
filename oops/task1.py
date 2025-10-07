class Car:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
car1=Car("BMW",500000)
car1.price=700000
print("car1's price is updated")
car2=Car("Ford",300000)
print(car1.__dict__)
print(car2.__dict__)



