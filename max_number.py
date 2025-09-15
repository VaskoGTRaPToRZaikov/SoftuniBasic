from sys import maxsize

max_num = -maxsize

while True:
    text = input()

    if text == "Stop":
        break

    else:
        number = int(text)

        if max_num < number:
            max_num = number

print(max_num)
