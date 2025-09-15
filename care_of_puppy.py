bought_food = int(input()) * 1000

needed_food = 0

while True:
    command = input()

    if command == "Adopted":
        break

    daily_food = int(command)
    needed_food += daily_food

if needed_food <= bought_food:
    print(f"Food is enough! Leftovers: {bought_food - needed_food} grams.")

else:
    print(f"Food is not enough. You need {abs(bought_food - needed_food)} grams more.")