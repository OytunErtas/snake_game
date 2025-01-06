with open("high_score.txt") as file:
    num = file.read()
    print(num)

with open("high_score.txt", mode="w") as file:
    file.write("anan")


with open("high_score.txt", mode="a") as file:
    file.write("\nbaban")