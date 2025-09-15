number = input()

for digit1 in range(1, int(number[2]) + 1):
    for digit2 in range(1, int(number[1]) + 1):
        for digit3 in range(1, int(number[0]) + 1):

            print(f"{digit1} * {digit2} * {digit3} = {digit1 * digit2 * digit3};")