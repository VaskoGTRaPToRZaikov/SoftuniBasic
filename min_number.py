from sys import maxsize

min_num = maxsize

while True:
    text = input()

    if text == "Stop":
        break

    else:
        number = int(text)

        if min_num > number:
            min_num = number

print(min_num)