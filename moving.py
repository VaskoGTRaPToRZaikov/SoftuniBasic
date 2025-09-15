space = int(input()) * int(input()) * int(input())

count_cubic_meters = 0

enough_space = False

while count_cubic_meters < space:
    command = input()

    if command == "Done":
        enough_space = True
        break

    else:
        cartons = int(command)
        count_cubic_meters += cartons

if enough_space:
    print(f"{abs(space - count_cubic_meters)} Cubic meters left.")

else:
    print(f"No more free space! You need {abs(space - count_cubic_meters)} Cubic meters more.")
