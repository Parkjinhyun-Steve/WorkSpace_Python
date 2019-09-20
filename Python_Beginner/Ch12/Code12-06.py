##
class Car:
    color = ""
    speed = 0
    count = 0

    def __init__(self):
        self.speed = 0
        Car.count += 1
    
##
myCar1, myCar2 = None, None

##
myCar1 = Car()
myCar1.speed = 30
print("Car1 %dkm, %d" % (myCar1.speed, myCar1.count))

myCar2 = Car()
myCar2.speed = 60
print("Car2 %dkm, %d" % (myCar2.speed, myCar2.count))
