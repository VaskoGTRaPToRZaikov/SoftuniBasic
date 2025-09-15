INITIAL_HEIGHT = 5364

days = 1
current_height = INITIAL_HEIGHT
success_climbed = False

while True:
    command = input()

    if command == "END":
        break

    if command == "Yes":
        days += 1

    if days > 5:
        break

    climbed_meters = int(input())

    current_height += climbed_meters

    if current_height >= 8848:
        success_climbed = True
        break

if success_climbed:
    print(f"Goal reached for {days} days!")

else:
    print(f"Failed!\n{current_height}")



