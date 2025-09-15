NEEDED_POINTS = 1250.5

name = input()
academy_points = float(input())
number_evaluative = int(input())

enough_points = False
current_points = academy_points

i = 0

while i < number_evaluative:
    evaluative_name = input()
    points = float(input())
    i += 1

    evaluative_points = (len(evaluative_name) * points) / 2
    current_points += evaluative_points

    if current_points > NEEDED_POINTS:
        enough_points = True
        break


if enough_points:
    print(f"Congratulations, {name} got a nominee for leading role with {current_points:.1f}!")

else:
    print(f"Sorry, {name} you need {NEEDED_POINTS - current_points:.1f} more!")
