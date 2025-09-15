MEN_GYM_PRICE = 42
MEN_BOXING_PRICE = 41
MEN_YOGA_PRICE = 45
MEN_ZUMBA_PRICE = 34
MEN_DANCES_PRICE = 51
MEN_PILATES_PRICE = 39
WOMEN_GYM_PRICE = 35
WOMEN_BOXING_PRICE = 37
WOMEN_YOGA_PRICE = 42
WOMEN_ZUMBA_PRICE = 31
WOMEN_DANCES_PRICE = 53
WOMEN_PILATES_PRICE = 37

budget = float(input())
gender = input()
age = int(input())
sport = input()

price = 0

if gender == "m":

    if sport == "Gym":
        price = MEN_GYM_PRICE

    elif sport == "Boxing":
        price = MEN_BOXING_PRICE

    elif sport == "Yoga":
        price = MEN_YOGA_PRICE

    elif sport == "Zumba":
        price = MEN_ZUMBA_PRICE

    elif sport == "Dances":
        price = MEN_DANCES_PRICE

    elif sport == "Pilates":
        price = MEN_PILATES_PRICE

elif gender == "f":

    if sport == "Gym":
        price = WOMEN_GYM_PRICE

    elif sport == "Boxing":
        price = WOMEN_BOXING_PRICE

    elif sport == "Yoga":
        price = WOMEN_YOGA_PRICE

    elif sport == "Zumba":
        price = WOMEN_ZUMBA_PRICE

    elif sport == "Dances":
        price = WOMEN_DANCES_PRICE

    elif sport == "Pilates":
        price = WOMEN_PILATES_PRICE

if age <= 19:
    price -= price * 0.20

if budget >= price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${price - budget:.2f} more.")