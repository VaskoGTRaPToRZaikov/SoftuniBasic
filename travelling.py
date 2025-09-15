while True:
    destination = input()

    if destination == "End":
        break

    needed_budget = float(input())
    current_budget = 0

    while True:

        income = float(input())

        current_budget += income

        if current_budget >= needed_budget:
            print(f"Going to {destination}!")
            current_budget = 0
            break



