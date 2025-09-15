days = int(input())
overall_food = float(input())

food_cat_sum = 0
food_dog_sum = 0
daily_consumation = 0
biscuit = 0

for i in range(1,days + 1):
    dog_eat = int(input())
    cat_eat = int(input())

    food_cat_sum += cat_eat
    food_dog_sum += dog_eat

    if i % 3 == 0:
        daily_consumation = dog_eat + cat_eat
        biscuit += daily_consumation * 0.10

total_consumation = food_dog_sum + food_cat_sum

percent_total_consumation = (food_cat_sum + food_dog_sum) / overall_food * 100
percent_cat_consumation = food_cat_sum / total_consumation * 100
percent_dog_consumation = food_dog_sum / total_consumation * 100

print(f"Total eaten biscuits: {round(biscuit)}gr.")
print(f"{percent_total_consumation:.2f}% of the food has been eaten.")
print(f"{percent_dog_consumation:.2f}% eaten from the dog.")
print(f"{percent_cat_consumation:.2f}% eaten from the cat.")

