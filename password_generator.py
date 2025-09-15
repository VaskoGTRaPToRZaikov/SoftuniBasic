n = int(input())
l = int(input())

for digit1 in range(1, n + 1):
    for digit2 in range(1, n + 1):
        for letter1 in range(l):
            for letter2 in range(l):
                for digit3 in range(1, n + 1):

                    if digit3 > digit1 and digit3 > digit2:

                        char1 = chr(97 + letter1)
                        char2 = chr(97 + letter2)

                        print(f"{digit1}{digit2}{char1}{char2}{digit3}", end=" ")