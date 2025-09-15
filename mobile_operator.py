ONE_YEAR_SMALL = 9.98
ONE_YEAR_MIDDLE = 18.99
ONE_YEAR_LARGE = 25.98
ONE_YEAR_EXTRALARGE = 35.99
TWO_YEAR_SMALL = 8.58
TWO_YEAR_MIDDLE = 17.09
TWO_YEAR_LARGE = 23.59
TWO_YEAR_EXTRALARGE = 31.79

term = input()
type_contract = input()
mobile_internet = input()
number_months = int(input())

price = 0

if term == "one":
    if type_contract == "Small":
        price = ONE_YEAR_SMALL
    elif type_contract == "Middle":
        price = ONE_YEAR_MIDDLE
    elif type_contract == "Large":
        price = ONE_YEAR_LARGE
    elif type_contract == "ExtraLarge":
        price = ONE_YEAR_EXTRALARGE
elif term == "two":
    if type_contract == "Small":
        price = TWO_YEAR_SMALL
    elif type_contract == "Middle":
        price = TWO_YEAR_MIDDLE
    elif type_contract == "Large":
        price = TWO_YEAR_LARGE
    elif type_contract == "ExtraLarge":
        price = TWO_YEAR_EXTRALARGE

if mobile_internet == "yes":
    if price <= 10:
        price += 5.50
    elif price <= 30:
        price += 4.35
    else:
        price += 3.85

overall_sum = price * number_months

if term == "two":
    overall_sum -= overall_sum * 0.0375

print(f"{overall_sum:.2f} lv.")

