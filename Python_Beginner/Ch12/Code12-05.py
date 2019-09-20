class Car:
    name =""
    speed = 0

    def __init__ (self, name, speed):
        self.name = name
        self.speed = speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

car1, car2 =  None, None

car1 = Car("audi" , 0)
car2 = Car("benz", 30)


print("%s   %dkm" %(car1.getName(), car1.getSpeed()))
print("%s   %dkm" %(car2.getName(), car2.getSpeed()))

