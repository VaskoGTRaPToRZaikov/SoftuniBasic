winner = ""
winner_points = 0
current_points = 0

while True:
    name = input()

    if name == "Stop":
        break

    for char in name:
        number = int(input())
        ascii_number = ord(char)

        if number == ascii_number:
            current_points += 10

        else:
            current_points += 2


    if winner_points <= current_points:
        winner_points = current_points
        winner = name

    current_points = 0

print(f"The winner is {winner} with {winner_points} points!")
