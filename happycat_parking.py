EVEN_DAY_ODD_HOUR = 2.50
ODD_DAY_EVEN_HOUR = 1.25
OTHERS = 1

days = int(input())
hours = int(input())

current_price = 0
overall_price = 0

for day in range(1, days + 1):
    for hour in range(1, hours + 1):

        if day % 2 == 0 and hour % 2 != 0:
            current_price += 2.50

        elif day % 2 != 0 and hour % 2 == 0:
            current_price += 1.25

        else:
            current_price += 1

    print(f"Day: {day} - {current_price:.2f} leva")
    overall_price += current_price
    current_price = 0

print(f"Total: {overall_price:.2f} leva")