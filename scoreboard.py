from turtle import Turtle
MOVE = False
ALLIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/Users/oytun/OneDrive/Desktop/high_score.txt") as file:
            self.high_score = int(file.read())
        self.color("Blue")
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.update_highscore()
        self.write(arg=f"Score: {self.score} High Score {self.high_score}", move = MOVE, align=ALLIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset_game(self):
        if self.score > self.high_score:
            with open("/Users/oytun/OneDrive/Desktop/high_score.txt", mode="w") as file:
                file.write(f"{self.score}")

        self.score = 0
        self.update_score()


    def update_highscore(self):
        with open("/Users/oytun/OneDrive/Desktop/high_score.txt") as file:
            self.high_score = int(file.read())


        # self.printed_score = f"Your score is: {self.score}"
        # self.write(self.printed_score, move=True, align="center", font=("Arial", 10, 'normal'))
        # self.hideturtle()
        #
        #
        # #
        #     # def game_over(self):
        #     #     self.goto(0, 0)
        #     #     self.write(arg="Game Over!", align=ALLIGNMENT,font=FONT)