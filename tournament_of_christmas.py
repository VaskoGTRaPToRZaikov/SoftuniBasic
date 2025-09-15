days = int(input())

wins_count = 0
loses_count = 0
daily_money = 0
winner_days = 0
loser_days = 0
overall_money = 0
tournament_winner = False

for day in range (1, days + 1):
    while True:
        sport = input()

        if sport == "Finish":
            break

        result = input()

        if result == "win":
            wins_count += 1
            daily_money += 20

        elif result == "lose":
            loses_count += 1

    if wins_count > loses_count:
        daily_money += daily_money * 0.10
        winner_days += 1

    else:
        loser_days += 1

    wins_count = 0
    loses_count = 0

    overall_money += daily_money
    daily_money = 0

if winner_days > loser_days:
    overall_money += overall_money * 0.20
    tournament_winner = True

if tournament_winner:
    print(f"You won the tournament! Total raised money: {overall_money:.2f}")

else:
    print(f"You lost the tournament! Total raised money: {overall_money:.2f}")