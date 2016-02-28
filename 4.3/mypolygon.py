"""Exercises, section 4.3, p.31"""

import turtle, math
bob = turtle.Turtle()

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
    t.ht()

def square(t, length):
    polygon(t, length, 4)

def arc(t, radius, angle):
    circumference = 2 * math.pi * radius
    side_length = circumference / 360
    for i in range(angle):
        t.fd(side_length)
        t.lt(1)
    t.ht()

def circle(t, radius):
    arc(t, radius, 360)

if __name__ == "__main__":
    circle(bob, 100)
    turtle.mainloop()