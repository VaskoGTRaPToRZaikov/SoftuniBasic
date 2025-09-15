n = int(input())

row = 1
while row <= n:

    if row == 1 or row == n:
        print("+ " + "- " * (n - 2) + "+")

    else:
        print("| " + "- " * (n - 2) + "|")

    row += 1
