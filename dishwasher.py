PREP_FOR_PLATE = 5
PREP_FOR_BOWL = 15

bottle_preparation = int(input()) * 750

was_enough = False
used_prep = 0
count_loads = 0
count_plates = 0
count_bowl = 0

while True:
    command = input()
    count_loads += 1

    if command == "End":
        was_enough = True
        break

    else:
        dishes = int(command)

        if count_loads % 3 == 0:
            used_prep += dishes * PREP_FOR_BOWL

        else:
            used_prep += dishes * PREP_FOR_PLATE

        if used_prep > bottle_preparation:
            break

        else:
            if count_loads % 3 == 0:
                count_bowl += dishes

            else:
                count_plates += dishes

prep_result = abs(bottle_preparation - used_prep)



if was_enough:
    print(f"Detergent was enough!\n{count_plates} dishes and {count_bowl} pots were washed.")
    print(f"Leftover detergent {prep_result} ml.")

else:
    print(f"Not enough detergent, {prep_result} ml. more necessary!")
