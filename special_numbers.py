START = 1111
END = 9999

number = int(input())

for num in range(START, END + 1):
    for digit in str(num):

        if digit == "0":
            break

        if number % int(digit) != 0:
            break

    else:
        print(num, end=" ")