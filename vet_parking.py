number_days = int(input())
hours_per_day = int(input())

day = 1
hours = 1
daily_fee = 0
total_fee = 0

while day < number_days + 1:
    while hours < hours_per_day + 1:
        if day % 2 == 0:
            if hours % 2 != 0:
                daily_fee += 2.50

            else:
                daily_fee += 1
            hours += 1
        else:
            if hours % 2 == 0:
                daily_fee += 1.25
            else:
                daily_fee += 1
            hours += 1

    print(f"Day: {day} - {daily_fee:.2f} leva")
    total_fee += daily_fee
    day += 1
    daily_fee = 0
    hours = 1

print(f"Total: {total_fee:.2f} leva")
