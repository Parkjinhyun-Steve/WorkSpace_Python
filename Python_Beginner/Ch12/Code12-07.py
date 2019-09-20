##
class Car:
    speed = 0
    def upSpeed(self, value):
        self.speed += value
        
        print("current speed(super class) : %d" % self.speed)

class Sedan(Car):
    def upSpeed(self, value):
        self.speed += value
        if self.speed > 150:
            self.speed = 150
            print("current speed(sub calss) : %d" % self.speed)



class Truck(Car):
    pass

##
sedan1, truck1 = None, None

## main code
truck1 = Truck()
sedan1 = Sedan()

print("T", end="")
truck1.upSpeed(200)

print("S", end="")
sedan1.upSpeed(200)