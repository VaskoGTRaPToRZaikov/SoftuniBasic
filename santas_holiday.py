ONE_PERSON_ROOM_PRICE = 18
APARTMENT_PRICE = 25
PRESIDENT_APARTMENT_PRICE = 35

days = int(input())
type_room = input()
grade = input()

overnights = days - 1
overnights_price = 0
price = 0

if type_room == "room for one person":
    price = ONE_PERSON_ROOM_PRICE
    overnights_price = overnights * price

elif type_room == "apartment":
    price = APARTMENT_PRICE
    overnights_price = overnights * price

    if days < 10:
        overnights_price -= overnights_price * 0.30

    elif 10 <= days <= 15:
        overnights_price -= overnights_price * 0.35

    else:
        overnights_price -= overnights_price * 0.50


elif type_room == "president apartment":
    price = PRESIDENT_APARTMENT_PRICE
    overnights_price = overnights * price

    if days < 10:
        overnights_price -= overnights_price * 0.10

    elif 10 <= days <= 15:
        overnights_price -= overnights_price * 0.15

    else:
        overnights_price -= overnights_price * 0.20


if grade == "positive":
    overnights_price += overnights_price * 0.25

elif grade == "negative":
    overnights_price -= overnights_price * 0.10

print(f"{overnights_price:.2f}")