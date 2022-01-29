import turtle
import random

w = 800
h = 600
fs = 10
d = 100  # milliseconds

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def r():
    global a_1, b, c, p
    a_1 = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    b = "up"
    c = nun()
    food.goto(c)
    hall()

def hall():
    global b

    new_head = a_1[-1].copy()
    new_head[0] = a_1[-1][0] + offsets[b][0]
    new_head[1] = a_1[-1][1] + offsets[b][1]

    if new_head in a_1[:-1]:
        r()
    else:
        a_1.append(new_head)

        if not c_1():
            a_1.pop(0)

        if a_1[-1][0] > w / 2:
            a_1[-1][0] -= w
        elif a_1[-1][0] < - w / 2:
            a_1[-1][0] += w
        elif a_1[-1][1] > h / 2:
            a_1[-1][1] -= h
        elif a_1[-1][1] < -h / 2:
            a_1[-1][1] += h

        p.clearstamps()
 #clears all the stamps

        for segment in a_1:
            p.goto(segment[0], segment[1])
            p.stamp()

        screen.update()
 #updates the turtle.screen screen

        turtle.ontimer(hall, d)

def c_1():
    global c
    if dist(a_1[-1], c) < 20:
        c = nun()
        food.goto(c)
        return True
    return False

def nun():
    x = random.randint(- w / 2 + fs, w / 2 - fs)
    y = random.randint(- h / 2 + fs, h / 2 - fs)
    return (x, y)

def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

def go_up():
    global b
    if b != "down":
        b = "up"

def go_right():
    global b
    if b != "left":
        b = "right"

def go_down():
    global b
    if b != "up":
        b = "down"

def go_left():
    global b
    if b != "right":
        b = "left"

screen = turtle.Screen()
screen.setup(w, h)
screen.title("snake")
screen.bgcolor("red")
screen.setup(800, 600)
screen.tracer(0)

p = turtle.Turtle("square")
p.penup()

food = turtle.Turtle()
food.shape("circle")
food.color("white")
food.shapesize(fs / 20)
food.penup()

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

r()
turtle.done()