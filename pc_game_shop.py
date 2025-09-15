n = int(input())

count_hearthstone = 0
count_fornite = 0
count_overwatch = 0
count_others = 0

for _ in range(n):
    game_name = input()

    if game_name == "Hearthstone":
        count_hearthstone += 1

    elif game_name == "Fornite":
        count_fornite += 1

    elif game_name == "Overwatch":
        count_overwatch += 1

    else:
        count_others += 1

percent_hearthstone = count_hearthstone / n * 100
percent_fornite = count_fornite / n * 100
percent_overwatch = count_overwatch / n * 100
percent_others = count_others / n * 100

print(f"Hearthstone - {percent_hearthstone:.2f}%")
print(f"Fornite - {percent_fornite:.2f}%")
print(f"Overwatch - {percent_overwatch:.2f}%")
print(f"Others - {percent_others:.2f}%")