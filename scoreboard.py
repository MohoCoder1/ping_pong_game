from turtle import Turtle
TEXT_FONT = ("Courier", 30, "normal")
TEXT_ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(0, 250)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", align=TEXT_ALIGN,
                   font=TEXT_FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

