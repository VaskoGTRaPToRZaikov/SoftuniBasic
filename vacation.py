needed_money = float(input())
available_money = float(input())

overall_days = 0
spend_days = 0
is_enough_money = False

while spend_days < 5:
    action = input()
    money = float(input())
    overall_days += 1

    if action == "spend":
        spend_days += 1
        available_money = available_money - money if available_money > money else 0

    elif action == "save":
        spend_days = 0
        available_money += money

        if available_money >= needed_money:
            is_enough_money = True
            break

if is_enough_money:
    print(f"You saved the money for {overall_days} days.")

else:
    print(f"You can't save the money.\n{overall_days}")