import turtle, math, time

def arc_radius(width, height):
    """Calculate radius of an arc given its width and height
    See: http://www.mathopenref.com/arcradiusderive.html"""
    return (height / 2) + ((width**2)/(8*height))

def segment_angle(chord_length, radius):
    """Calculates segment angle give chord length and arc radius
    See: https://en.wikipedia.org/wiki/Circular_segment"""
    radians = 2 * math.asin(chord_length / (2 * radius))
    return math.degrees(radians)

def petal(t, length, width):
    """Draw a petal, by drawing an arc, turning the turtle and drawing an
    identical arc back to the starting point.
    't' is a turtle.Turtle instance.
    'length' is an integer representing pixels.
    'width' is a float between 0 and 1, a fraction of 'length'"""
    width_of_petal = length * width
    height_of_arc = width_of_petal / 2
    radius = arc_radius(width=length, height=height_of_arc)
    angle = segment_angle(chord_length=length, radius=radius)
    
    #Draw petal
    t.circle(radius=radius, extent=angle)
    t.lt(180 - angle)
    t.circle(radius=radius, extent=angle)

def flower(t, petal_length, petal_width, npetals):
    heading = t.heading()
    increment = 360 / npetals
    for i in range(npetals):
        petal(t, petal_length, petal_width)
        heading += increment
        t.setheading(heading)

if __name__ == "__main__":
    bob = turtle.Turtle()
    flower(bob, petal_length=150, petal_width=0.4, npetals=12)
    bob.ht()
    time.sleep(3)
    bob.st()
    bob.reset()
    flower(bob, petal_length=150, petal_width=0.1, npetals=20)
    bob.ht()
    time.sleep(3)
    bob.st()
    bob.reset()
    flower(bob, petal_length=100, petal_width=0.2, npetals=15)
    bob.ht()
    turtle.mainloop()