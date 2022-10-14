from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# when the turtle hits the top edge of the screen, it moves back to the original position and the player levels up
# on the next level, the car speed increases
# when the


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.level = 0
        self.go_to_start()
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True

    def go_to_start(self):
        self.goto(STARTING_POSITION)

