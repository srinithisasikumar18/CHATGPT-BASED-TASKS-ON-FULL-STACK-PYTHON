class Car:
    def __init__(self,make,model,year,speed=0):
        self.make=make
        self.model=model
        self.year=year
        self.speed=speed
    def accerlerate(self):
        self.speed=self.speed+5
        print(f"{self.make} runs in a speed of {self.speed}")
    def brake(self):
        self.speed=self.speed-5
        if self.speed<=0:
            self.speed=0
        print(f"{self.make} brake applied speed is {self.speed}")
    def display_speed(self):
        print(f"{self.make} is moving at speed of {self.speed}")
c1=Car("Toyato","Corolla",2020)
c2=Car("Honda","Civic",2022)
c1.accerlerate()
c1.brake()
c1.display_speed()
c2.accerlerate()
c2.accerlerate()
c2.brake()
c2.display_speed()
