a1 = int(input())
a2 = int(input())
n = int(input())

for letter in range(a1, a2):
    symbol1 = chr(letter)

    for digit1 in range(1, n):
        for digit2 in range(1, n // 2):
            digit3 = letter

            if letter % 2 != 0 and (digit1 + digit2 + digit3) % 2 != 0:
                print(f"{symbol1}-{digit1}{digit2}{digit3}")

