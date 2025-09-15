SMALL_WM_PRICE = 56
BIG_WM_PRICE = 28.70
SMALL_MANGO_PRICE = 36.66
BIG_MANGO_PRICE = 19.60
SMALL_PINEAPPLE_PRICE = 42.10
BIG_PINEAPPLE_PRICE = 24.80
SMALL_RASPBERRY_PRICE = 20
BIG_RASPBERRY_PRICE = 15.20

fruit = input()
set_size = input()
number_sets = int(input())

price = 0
number_boosters = 0

if fruit == "Watermelon":
    if set_size == "small":
        price = SMALL_WM_PRICE
        number_boosters = number_sets * 2
    elif set_size == "big":
        price = BIG_WM_PRICE
        number_boosters = number_sets * 5
elif fruit == "Mango":
    if set_size == "small":
        price = SMALL_MANGO_PRICE
        number_boosters = number_sets * 2
    elif set_size == "big":
        price = BIG_MANGO_PRICE
        number_boosters = number_sets * 5
elif fruit == "Pineapple":
    if set_size == "small":
        price = SMALL_PINEAPPLE_PRICE
        number_boosters = number_sets * 2
    elif set_size == "big":
        price = BIG_PINEAPPLE_PRICE
        number_boosters = number_sets * 5
elif fruit == "Raspberry":
    if set_size == "small":
        price = SMALL_RASPBERRY_PRICE
        number_boosters = number_sets * 2
    elif set_size == "big":
        price = BIG_RASPBERRY_PRICE
        number_boosters = number_sets * 5

overall_payment = price * number_boosters

if 400 <= overall_payment <= 1000:
    overall_payment -= overall_payment * 0.15
elif overall_payment > 1000:
    overall_payment -= overall_payment * 0.50

print(f"{overall_payment:.2f} lv.")


