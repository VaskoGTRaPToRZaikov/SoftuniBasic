cake_size = int(input()) * int(input())

count_pieces = 0
enough_pieces = False

while count_pieces < cake_size:
    command = input()

    if command == "STOP":
        enough_pieces = True
        break

    else:
        pieces = int(command)
        count_pieces += pieces

if enough_pieces:
    print(f"{abs(cake_size - count_pieces)} pieces are left.")

else:
    print(f"No more cake left! You need {abs(cake_size - count_pieces)} pieces more.")
