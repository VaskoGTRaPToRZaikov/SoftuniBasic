border_hundreds = int(input())
border_tens = int(input())
border_ones = int(input())

for hundreds in range(1, border_hundreds + 1):
    if hundreds % 2 == 0:

        for tens in range(1, border_tens + 1):
            is_prime = False

            if 2 <= tens <= 7:
                if tens == 2:
                    is_prime = True

                else:
                    for i in range(2, tens):
                        if tens % i == 0:
                            is_prime = False
                            break

                        else:
                            is_prime = True

            if is_prime:

                for ones in range(1, border_ones + 1):
                    if ones % 2 == 0:

                        print(f"{hundreds} {tens} {ones}")