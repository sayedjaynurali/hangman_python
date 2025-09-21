from turtle import Turtle

class HangmanDrawing:
    def __init__(self):
        self.tim = Turtle()
        self.tim.shape("turtle")
        self.tim.shapesize(1.5)

    def draw_gallows(self):
        self.tim.reset()
        self.tim.hideturtle()
        self.tim.speed(0)
        self.tim.penup()
        self.tim.goto(-100, -150)
        self.tim.pendown()
        self.tim.forward(200)
        self.tim.back(100)
        self.tim.left(90)
        self.tim.forward(300)
        self.tim.right(90)
        self.tim.forward(100)
        self.tim.right(90)
        self.tim.forward(50)

    def draw_head(self):
        self.tim.right(90)
        self.tim.circle(25)

    def draw_body(self):
        self.tim.left(90)
        self.tim.penup()
        self.tim.forward(50)
        self.tim.pendown()
        self.tim.forward(80)

    def draw_left_arm(self):
        self.tim.back(40)
        self.tim.left(45)
        self.tim.forward(50)
        self.tim.back(50)
        self.tim.right(45)

    def draw_right_arm(self):
        self.tim.right(45)
        self.tim.forward(50)
        self.tim.back(50)
        self.tim.left(45)

    def draw_left_leg(self):
        self.tim.forward(40)
        self.tim.left(30)
        self.tim.forward(60)
        self.tim.back(60)
        self.tim.right(30)

    def draw_right_leg(self):
        self.tim.right(30)
        self.tim.forward(60)
        self.tim.back(60)
        self.tim.left(30)
