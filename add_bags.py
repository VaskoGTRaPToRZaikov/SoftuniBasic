price_baggage_over_twenty = float(input())
baggage_kilograms = float(input())
days_before_travel = int(input())
number_baggage = int(input())

price = 0

if baggage_kilograms < 10:
    price = price_baggage_over_twenty * 0.20
elif 10 <= baggage_kilograms <= 20:
    price = price_baggage_over_twenty * 0.50
else:
    price = price_baggage_over_twenty

if days_before_travel > 30:
    price += price * 0.10
elif 7 <= days_before_travel <= 30:
    price += price * 0.15
else:
    price += price * 0.40

final_payment = price * number_baggage

print(f"The total price of bags is: {final_payment:.2f} lv. ")