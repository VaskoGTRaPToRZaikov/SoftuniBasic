FUEL_PRICE = 2.10
GUIDE_PRICE = 100

budget = float(input())
needed_fuel = float(input())
day = input()

discount = 0
overall_fuel_price = needed_fuel * FUEL_PRICE
expenses = overall_fuel_price + GUIDE_PRICE

if day == "Saturday":
    discount = 0.10
    expenses -= expenses * discount
elif day == "Sunday":
    discount = 0.20
    expenses -= expenses * discount

if budget >= expenses:
    print(f"Safari time! Money left: {budget - expenses:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {expenses - budget:.2f} lv.")


