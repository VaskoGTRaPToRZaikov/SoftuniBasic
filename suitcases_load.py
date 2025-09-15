capacity = float(input())

free_capacity = capacity
count_suitcases = 0

while True:
    command = input()

    if command == "End":
        print("Congratulations! All suitcases are loaded!")
        break

    suitcase_volume = float(command)

    if (count_suitcases + 1) % 3 == 0:
        suitcase_volume *= 1.10

    if free_capacity < suitcase_volume:
        print("No more space!")
        break

    free_capacity -= suitcase_volume
    count_suitcases += 1

print(f"Statistic: {count_suitcases} suitcases loaded.")