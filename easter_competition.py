easter_breads = int(input())

bakers = 0
number_one = 0
winner_name = ""

while bakers < easter_breads:
    baker_name = input()
    baker_overall_grades = 0
    bakers+= 1

    while True:
        grades = input()

        if grades == "Stop":
            print(f"{baker_name} has {baker_overall_grades} points.")

            if number_one < baker_overall_grades:
                number_one = baker_overall_grades
                winner_name = baker_name
                print(f"{baker_name} is the new number 1!")

            break

        else:
            baker_overall_grades += int(grades)

print(f"{winner_name} won competition with {number_one} points!")

