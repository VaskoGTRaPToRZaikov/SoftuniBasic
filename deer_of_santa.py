import math

days = int(input())
food = int(input())
first_deer_daily_food = float(input())
second_deer_daily_food = float(input())
third_deer_daily_food = float(input())

needed_food = days * first_deer_daily_food + days * second_deer_daily_food + days * third_deer_daily_food

diff = abs(food - needed_food)

if needed_food <= food:
    print(f"{math.floor(diff)} kilos of food left.")

else:
    print(f"{math.ceil(diff)} more kilos of food are needed.")