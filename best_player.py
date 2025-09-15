hat_trick_count = 0
best_player = ""
best_player_goals = 0

while True:
    name = input()

    if name == "END":
        break

    else:
        goals = int(input())

        if goals >= 3:
            hat_trick_count += 1

        if goals > best_player_goals:
            best_player_goals = goals
            best_player = name

        if goals >= 10:
            break

if hat_trick_count > 0:
    print(f"{best_player} is the best player!")
    print(f"He has scored {best_player_goals} goals and made a hat-trick !!!")

else:
    print(f"{best_player} is the best player!")
    print(f"He has scored {best_player_goals} goals.")