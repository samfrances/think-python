"""Answer to exercise 4.4, p.38"""

import math, turtle

def polar2cart(r, theta):
    """Math: https://www.mathsisfun.com/polar-cartesian-coordinates.html
    theta in radians"""
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y

def arch_math(r, a, b):
    """Based on polar equation for Archimedean spiral:
    r = a + (b * theta)

    See: https://en.wikipedia.org/wiki/Archimedean_spiral
    """
    theta = (r - a) / b
    return theta

def draw_arch_spiral(t, a, b, r):
    """Draw an Archimedean spiral.

    Args:
      t: turtle
      a: from spiral equation r = a + (b * theta)
      b: from spiral equation r = a + (b * theta)
      r = largest value of r for r = a + (b * theta)

    """

    for i in range(r*10):
        i = i / 10
        next_point = polar2cart(i, arch_math(i, a, b))
        t.goto(next_point)

if __name__ == "__main__":

    bob = turtle.Turtle()
    draw_arch_spiral(bob, 1, 3, 200)
    turtle.mainloop()
    