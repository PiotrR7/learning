from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.refresh()

    def refresh(self):
        shape = random.choice(['circle', 'square', 'triangle'])
        color = random.choice(['red', 'green', 'blue'])

        self.hideturtle()
        self.shape(shape)
        self.color(color)
        self.goto(
            x = random.randint(-200, 200),
            y = random.randint(-200, 200)
        )
        self.showturtle()