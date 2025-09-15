TARGET_STEPS = 10_000

count_steps = 0

while count_steps < TARGET_STEPS:
    command = input()

    if command == "Going home":
        steps = int(input())
        count_steps += steps
        break

    else:
        steps = int(command)
        count_steps += steps

result = abs(TARGET_STEPS - count_steps)

if count_steps >= TARGET_STEPS:
    print(f"Goal reached! Good job!\n{result} steps over the goal!")

else:
    print(f"{result} more steps to reach goal.")
