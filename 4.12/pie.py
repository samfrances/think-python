"""Exercise 4.3, p.37"""

from polygon import polygon
import turtle, math

def segment(t, angle, base_length):
    """Draw a pie segment, (an isosceles triangle), given the third angle and
    base length. 't' is a turtle"""
    
    # Calculate relevant numbers for isosceles triangle
    # Maths: http://math.stackexchange.com/a/272157
    base_angles = (180 - angle) / 2
    height = (base_length / 2) * math.tan(math.radians(base_angles))
    side_length = math.sqrt((height**2) + ((base_length/2)**2))
    
    t.fd(side_length)
    t.lt(180 - base_angles)
    t.fd(base_length)
    t.lt(180 - base_angles)
    t.fd(side_length)

def pie(t, nsides, lsides):
    """Draw an n-sides polygon with 'spokes'.
    't' is a turtle.
    'nsides' is the number of sides.
    'lsides' is the length of the sides'"""

    centre_angle = 360 / nsides
    lt_after_segment = 360 - ((centre_angle * 2) + 180)
    
    for i in range(nsides):
        segment(t, centre_angle, lsides)
        t.lt(lt_after_segment)

if __name__ == "__main__":
    bob = turtle.Turtle()
    bob.shape('turtle')
    pie(bob, 100, 10)
    bob.ht()
    turtle.mainloop()