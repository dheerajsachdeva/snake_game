from turtle import Turtle


class Scorecard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.write(f"Score : {self.score}",  align="center", font=('Arial', 12, 'normal'))
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=('Arial', 12, 'normal'))


    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=('Arial', 12, 'normal'))


