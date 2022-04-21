from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.game_level = 0
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.write(f"Level: {self.game_level}", align="center", font= FONT)
        self.next_level()

    def next_level(self):
        self.game_level += 1
        self.clear()
        self.write(f"Level: {self.game_level}", align="center", font= FONT)

    def game_over(self):
        self.gameover = Turtle()
        self.gameover.write("GAME OVER", align="center", font=FONT)

