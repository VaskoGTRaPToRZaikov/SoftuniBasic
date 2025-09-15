initial_money = 7500

profit = 0
loss = 0
trades = 0
win_trades = 0

current_money = initial_money

while current_money > 1500:
    command = input().lower()

    if command == "end":
        break


    elif command == "profit":
        multiplier = int(input()) / 100
        profit += 1500 * multiplier
        current_money += 1500 * multiplier
        trades += 1
        win_trades += 1

    elif command == "loss":
        loss += 1500 * 0.20
        current_money -= 1500 * 0.20
        trades += 1

win_rate = win_trades / trades * 100

print(f"{win_rate:.2f}%")
print(f"{current_money:.2f}")

if profit > loss:
    print(f"Overall profit {abs(initial_money - current_money):.2f}")

else:
    print(f"Overall loss {abs(initial_money - current_money):.2f}")
