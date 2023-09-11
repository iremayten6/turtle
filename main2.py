import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
colours = ["CornflowerBlue", "DarkOrchid", "red","blue", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat",
           "SlateGray", "SeaGreen"]
#num_sides = 6
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.left(angle)
#         #tim.circle(2)
#
#
# for shape_side_n in range(3,11):
#     tim.speed(3)
#     tim.pensize(8)
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)


directions = [0, 90, 270, 360]
tim.pensize(6)
tim.speed("normal")

for _ in range(50):
    tim.color(random.choice(colours))
    tim.forward(20)
    tim.setheading(random.choice(directions))


