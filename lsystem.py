import turtle
import time
import random
import math

from collections import defaultdict

seed = time.time()

tropism_angle = 0
tropism_amount = 0
angle_random_variation = 0
length_random_variation = 0

bud_symbols = []

default_pen_size = 2
line_length = 10
start_pos = (0, -380)

sub_chance = 1.0

def get_map(rules, char):
    if char in rules and random.random() < sub_chance:
        return rules[char]
    else:
        return char

def get_symbols(rules, axiom, iterations):
    random.seed(seed)

    symbols = axiom

    for i in range(iterations):
        symbols = "".join(get_map(rules, char) for char in symbols)

    return symbols

def run(lindenmayer, symbols, dist, angle):
    random.seed(seed)

    stack = []

    for char in symbols:
        if char == "[":
            stack.append((lindenmayer.heading(), lindenmayer.pos()))
        elif char == "]":
            (h, p) = stack.pop()
            should_hide = lindenmayer.isvisible()
            lindenmayer.hideturtle()
            lindenmayer.penup()
            lindenmayer.setheading(h)
            lindenmayer.setpos(p)
            lindenmayer.pendown()
            if should_hide:
                lindenmayer.showturtle()
        elif char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            lindenmayer.forward(dist)
            if length_random_variation > 0:
                lindenmayer.forward(random.gauss(dist, length_random_variation))
        elif char == "+":
            lindenmayer.right(angle)
        elif char == "-":
            lindenmayer.left(angle)

        if char in bud_symbols:
            lindenmayer.color(1, 1, 1)
            lindenmayer.pensize(7)
            lindenmayer.fd(1)
            lindenmayer.pensize(default_pen_size)
            lindenmayer.color(0.3, 0.5, 0.2)

        # random variation
        if angle_random_variation > 0:
            lindenmayer.right(random.gauss(0, angle * angle_random_variation))

        # tropism

        hd = lindenmayer.heading()
        if hd > 180:
            hd = 180 - hd

        tropism_delta = hd - tropism_angle
        lindenmayer.right(tropism_delta * tropism_amount)


print("Available L-systems:")
for tree in ["1) Fern", "2) Binary Tree", "3) Cow Parsley (default)", "4) Hilbert Curve", "5) George bush"]:
    print("  ↳", tree)
pickedSystem = input("\nWhich of the above? > ").lower()
# fern
if pickedSystem in ["1", "fern"]:
    rules = {
        "X": "Y+[[X]-X]-Y[-YX]+X",
        "Y": "YY"
    }
    axiom = "X"
    angle = 20

# binary tree
elif pickedSystem in ["2", "biary", "tree", "binary tree"]:
    rules = {
        "X": "XX",
        "Y": "X[-Y][+Y]"
    }
    axiom = "Y"
    angle = 30
    line_length = 30
    default_pen_size = 5

    tropism_angle = 60
    tropism_amount = 0.05
    angle_random_variation = 0.05
    length_random_variation = 3

# cow parsley
elif pickedSystem in ["3", "cow parsley", "cow", "parsley"]:
    rules = {
        # base growth and flowers
        "F": "XY[++G][--G][G]",
        "G": "XX[++G][--G][G]",

        # leave shoot timing
        "X": "XX",
        "Y": "YZ",
        "Z": "[++++L]X[----L]X",

        # leaves
        "L": "MM[+++L][---L]L",
        "M": "MMM"
    }
    axiom = "F"
    angle = 20
    line_length = 2
    tropism_angle = 70
    tropism_amount = 0.01
    angle_random_variation = 0.07
    default_pen_size = 2
    length_random_variation = 2
    bud_symbols = "FG"
    start_pos = (-100, -380)

# hilbert curve
elif pickedSystem in ["4", "hilbert curve", "hilbert", "curve"]:
    rules = {
        "a": "+bX-aXa-Xb+",
        "b": "-aX+bXb+Xa-"
    }
    axiom = "a"
    angle = 90
    start_pos = (-350, -350)
    default_pen_size = 2
    line_length = 11

# George bush
elif pickedSystem in ["5", "george bush", "george", "bush"]:
    rules = {
        "X": "XX+[+X-X-X]-[-X+X+X]"
    }
    axiom = "X"
    angle = 20
    angle_random_variation = 0.07
    default_pen_size = 1
    line_length = 8
    length_random_variation = 4
    tropism_angle = 120
    tropism_amount = 0.005


### Default, feel free to customise to make your own :) ├-------------------------------------
else:
    print("running default")
    rules = {
        # base growth and flowers
        "F": "XY[++G][--G][G]",
        "G": "XX[++G][--G][G]",

        # leave shoot timing
        "X": "XX",
        "Y": "YZ",
        "Z": "[++++L]X[----L]X",
        
        # leaves
        "L": "MM[+++L][---L]L",
        "M": "MMM"
    }
    axiom = "F"
    angle = 20
    line_length = 2
    tropism_angle = 70
    tropism_amount = 0.01
    angle_random_variation = 0.07
    default_pen_size = 2
    length_random_variation = 2
    bud_symbols = "FG"
    start_pos = (-100, -380)

### the actual code   ├-------------------------------------------------------------------------

print()    

symbols = axiom

win = turtle.Screen()
win.title("L-Systems")
win.setup(800, 800)
win.bgcolor(0.9, 0.83, 0.7)

lindenmayer = turtle.Turtle()
lindenmayer.color(0.3, 0.5, 0.2)
lindenmayer.pensize(default_pen_size)

def fast_mode():
    global win, lindenmayer
    print("Fast mode")
    win.tracer(0, 0)
    lindenmayer.hideturtle()
    lindenmayer.speed("fastest")

def slow_mode():
    global win, lindenmayer
    print("Slow mode")
    win.tracer(1, 25)
    lindenmayer.showturtle()
    lindenmayer.turtlesize(2)
    lindenmayer.speed("slow")

def iterate():
    global symbols

    lindenmayer.clear()
    lindenmayer.penup()
    lindenmayer.goto(start_pos)
    lindenmayer.setheading(90)
    lindenmayer.pendown()

    run(lindenmayer, symbols, line_length, angle)
    win.update()

    symbols = get_symbols(rules, symbols, 1)

fast_mode()

iterate()

print("ENTER to advance")
print("UP for fast mode")
print("DOWN for slow mode")

win.onkey(iterate, "Return")
win.onkey(fast_mode, "Up")
win.onkey(slow_mode, "Down")

win.listen()
win.mainloop()
