first_num_border = int(input())
second_num_border = int(input())
third_num_border = int(input())

for num1 in range(1, first_num_border + 1):
    if num1 % 2 == 0:

        for num2 in range(1, second_num_border + 1):
            is_prime = False

            if 2 <= num2 <= 7:

                if num2 == 2:
                    is_prime = True

                else:

                    for i in range(2, num2):
                        if num2 % i == 0:
                            is_prime = False
                            break

                        else:
                            is_prime = True

            if is_prime:

                    for num3 in range(1, third_num_border + 1):
                            if num3 % 2 == 0:
                                print(f"{num1} {num2} {num3}")
