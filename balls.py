import math

RED_POINTS = 5
ORANGE_POINTS = 10
YELLOW_POINTS = 15
WHITE_POINTS = 20

n = int(input())

count_red = 0
count_orange = 0
count_yellow = 0
count_white = 0
count_black = 0
count_others = 0
overall_points = 0

for _ in range(n):
    color_balls = input()

    if color_balls == "red":
        count_red += 1
        overall_points += 5

    elif color_balls == "orange":
        count_orange += 1
        overall_points += 10

    elif color_balls == "yellow":
        count_yellow += 1
        overall_points += 15

    elif color_balls == "white":
        count_white += 1
        overall_points += 20

    elif color_balls == "black":
        count_black += 1
        overall_points = math.floor(overall_points / 2)

    else:
        count_others += 1

print(f"Total points: {overall_points}")
print(f"Red balls: {count_red}")
print(f"Orange balls: {count_orange}")
print(f"Yellow balls: {count_yellow}")
print(f"White balls: {count_white}")
print(f"Other colors picked: {count_others}")
print(f"Divides from black balls: {count_black}")