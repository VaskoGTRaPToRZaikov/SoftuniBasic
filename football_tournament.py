club_name = input()
number_games = int(input())

if number_games == 0:
    print(f"{club_name} hasn't played any games during this season.")
else:
    count_wins = 0
    count_draws = 0
    count_loses = 0
    overall_points = 0

    for _ in range(number_games):
        result = input()

        if result == "W":
            count_wins += 1
            overall_points += 3
        elif result == "D":
            count_draws += 1
            overall_points += 1
        elif result == "L":
            count_loses += 1

    percent_wins = count_wins / number_games * 100

    print(f"{club_name} has won {overall_points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {count_wins}")
    print(f"## D: {count_draws}")
    print(f"## L: {count_loses}")
    print(f"Win rate: {percent_wins:.2f}%")