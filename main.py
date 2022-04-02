"""
Python program thats draw Sierpinski triangle
(https://en.wikipedia.org/wiki/Sierpinski_triangle)

Code made by ExclMark
(https://github.com/ExclMark)
"""

# Import turtle for drawing
import turtle
# Import random for selecting random dot
import random

# Setup turtle
screen_x = 1920
screen_y = 1080

A_point_x = 0
A_point_y = 300
B_point_x = 400
B_point_y = -300
C_point_x = -400
C_point_y = -300
turtle.setup(screen_x, screen_y)
turtle.penup()

# Draw dot using turtle
def draw_dot(x, y):
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()
    turtle.penup()
    return x, y

# Draw line from dot to dot
def draw_line(x1, y1, x2, y2):
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.penup()

# Draw triangle
def prepare():
    draw_dot(A_point_x, A_point_y)
    draw_dot(B_point_x, B_point_y)
    draw_dot(C_point_x, C_point_y)

    draw_line(C_point_x, C_point_y, A_point_x, A_point_y)
    draw_line(A_point_x, A_point_y, B_point_x, B_point_y)
    draw_line(B_point_x, B_point_y, C_point_x, C_point_y)

# Calculate area of triangle
def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) +
                x2 * (y3 - y1) +
                x3 * (y1 - y2)) / 2.0)

# Is point inside of triangle
def isInside(x, y):
    A = area(A_point_x, A_point_y, B_point_x, B_point_y, C_point_x, C_point_y)
    A1 = area(x, y, B_point_x, B_point_y, C_point_x, C_point_y)
    A2 = area(A_point_x, A_point_y, x, y, C_point_x, C_point_y)
    A3 = area(A_point_x, A_point_y, B_point_x, B_point_y, x, y)
    return A == A1 + A2 + A3

# Draw random dot
def draw_random_dot():
    while True:
        x = random.randint(C_point_x, B_point_x)
        y = random.randint(C_point_y, A_point_y)
        if isInside(x, y):
            draw_dot(x, y)
            turtle.update()
            return x, y
        else: continue

# Choose random triangle vertex
def select_vertex():
    x = random.choice([A_point_x, B_point_x, C_point_x])
    y = A_point_y if x == A_point_x else B_point_y if x == B_point_x else C_point_y
    return x, y

# Find middle point from point (x, y) and point (x1, y1)
def find_middle(x, y, x1, y1):
    x_middle = (x + x1) / 2
    y_middle = (y + y1) / 2
    return x_middle, y_middle

# Draw triangle
prepare()

# Set drawing speed to max
turtle.speed(0)

# Draw random dot
x, y = draw_random_dot()

# Variable to store number of dots
number_of_dots = 0

while True:
    x_v, y_v = select_vertex()
    x_m, y_m = find_middle(x, y, x_v, y_v)
    x, y = draw_dot(x_m, y_m)
    number_of_dots += 1
    print(f"Dot number: {number_of_dots}, x: {x}, y: {y}")