PRICE_90X130 = 110
PRICE_100X150 = 140
PRICE_130X180 = 190
PRICE_200X300 = 250

number_joinery = int(input())
kind_joinery = input()
kind_delivery = input()

price = 0
delivery = 0

if number_joinery < 10:
    print("Invalid order")

else:
    if kind_joinery == "90X130":
        if number_joinery <= 30:
            price = PRICE_90X130
        elif number_joinery <= 60:
            price = PRICE_90X130 * 0.95
        else:
            price = PRICE_90X130 * 0.92

    elif kind_joinery == "100X150":
        if number_joinery <= 40:
            price = PRICE_100X150
        elif number_joinery <= 80:
            price = PRICE_100X150 * 0.94
        else:
            price = PRICE_100X150 * 0.90

    elif kind_joinery == "130X180":
        if number_joinery <= 20:
            price = PRICE_130X180
        elif number_joinery <= 50:
            price = PRICE_130X180 * 0.93
        else:
            price = PRICE_130X180 * 0.88

    elif kind_joinery == "200X300":
        if number_joinery <= 25:
            price = PRICE_200X300
        elif number_joinery <= 50:
            price = PRICE_200X300 * 0.91
        else:
            price = PRICE_200X300 * 0.86

    if kind_delivery == "With delivery":
        delivery = 60
    elif kind_delivery == "Without delivery":
        delivery = 0

    overall_price = number_joinery * price + delivery

    if number_joinery > 99:
        overall_price -= overall_price * 0.04

    print(f"{overall_price:.2f} BGN")