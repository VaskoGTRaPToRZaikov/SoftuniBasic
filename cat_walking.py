BURN_CALORIES_PER_MINUTE = 5

walking_time = int(input())
number_walks = int(input())
cat_calories = int(input())

overall_walking_time = walking_time * number_walks

burned_calories = overall_walking_time * BURN_CALORIES_PER_MINUTE

half_cat_calories = cat_calories * 0.50

if burned_calories >= half_cat_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")