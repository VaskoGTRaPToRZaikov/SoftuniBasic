n = int(input())

current_num = 1
current_is_bigger = False

for row in range(1, n + 1):
    for col in range(1, row + 1):

        if current_num > n:
            current_is_bigger = True
            break

        print(current_num, end=" ")
        current_num += 1

    if current_is_bigger:
        break


    print()
