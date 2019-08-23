import turtle as t
import random

t.shape('turtle')
t.speed(1)

for x in range (5000000):
    a=random.randint(1, 360)
    t.setheading(a)
    b=random.randint(1,20)
    t.forward(b)
    
