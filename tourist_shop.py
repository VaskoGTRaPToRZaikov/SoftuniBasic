budget = float(input())

current_sum = 0
count_products = 0
needed_money = 0

while True:
    product_name = input()

    if product_name == "Stop":
        print(f"You bought {count_products} products for {current_sum:.2f} leva.")
        break

    product_price = float(input())

    if (count_products + 1) % 3 == 0:
        product_price *= 0.50

    if product_price + current_sum > budget:
        needed_money = product_price + current_sum - budget
        print(f"You don't have enough money!\nYou need {needed_money:.2f} leva!")
        break

    current_sum += product_price
    count_products += 1
