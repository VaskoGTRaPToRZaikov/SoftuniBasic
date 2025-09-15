first_start = int(input())
second_start = int(input())
first_diff = int(input())
second_diff = int(input())

first_end = first_start + first_diff
second_end = second_start + second_diff

for num1 in range(first_start, first_end + 1):
    for num2 in range(second_start, second_end + 1):

        is_prime = True

        for i in range(2, num1):
            for y in range(2, num2):

                    if num1 % i == 0 or num2 % y == 0:
                        is_prime = False
                        break

        if is_prime:
            print(f"{num1}{num2}")