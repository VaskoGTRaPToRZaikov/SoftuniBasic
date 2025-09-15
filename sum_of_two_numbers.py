start = int(input())
end = int(input())
magic_number = int(input())

count_combination = 0

has_magic_combination = False

for num1 in range(start, end + 1):
    for num2 in range(start, end + 1):

        count_combination += 1

        if (num1 + num2) == magic_number:
            print(f"Combination N:{count_combination} ({num1} + {num2} = {magic_number})")
            has_magic_combination = True
            break

    if has_magic_combination:
        break

if not has_magic_combination:
    print(f"{count_combination} combinations - neither equals {magic_number}")
