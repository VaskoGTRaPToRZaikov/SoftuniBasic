n = int(input())

first_num = int(input())
second_num = int(input())

reference_value = first_num + second_num
previous_value = reference_value

all_equal = True
max_diff = 0

for _ in range(n-1):
    num1 = int(input())
    num2 = int(input())

    current_value = num1 + num2

    if  current_value != previous_value:
        all_equal = False

    diff = abs(current_value - previous_value)

    if diff > max_diff:
        max_diff = diff

    previous_value = current_value

if all_equal:
    print(f"Yes, value={reference_value}")
else:
    print(f"No, maxdiff={max_diff}")

