number = int(input())

for num1 in range(1, 10):
    for num2 in range(1, 10):
        for num3 in range(1, 10):
            for num4 in range(1, 10):

                first_sum = num1 + num2
                second_sum = num3 + num4

                if first_sum == second_sum:

                    if number % first_sum == 0:

                        print(f"{num1}{num2}{num3}{num4}", end=" ")