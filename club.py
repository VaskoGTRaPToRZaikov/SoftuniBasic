desired_profit = float(input())

current_profit = 0

while True:
    cocktail_name = input()

    if cocktail_name == "Party!":
        print(f"We need {desired_profit - current_profit:.2f} leva more.")
        break
    else:
        number_cocktails = int(input())
        order_sum = number_cocktails * len(cocktail_name)
        if order_sum % 2 != 0:
            current_profit += order_sum * 0.75
        else:
            current_profit += order_sum

        if current_profit >= desired_profit:
                print(f"Target acquired.")
                break

print(f"Club income - {current_profit:.2f} leva.")

