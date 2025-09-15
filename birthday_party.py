hall_rent = float(input())

cake_price = hall_rent * 0.20
drinks_price = cake_price * 0.55
animator_price = hall_rent / 3

needed_budget = hall_rent + cake_price + drinks_price + animator_price

print(f"{needed_budget:.1f}")