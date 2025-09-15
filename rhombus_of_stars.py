n = int(input())

row = 1


while row <= n:
    print(" " * (n - row) + "*" + " *" * (row - 1))
    row += 1

row = n - 1
while row >= 1:
    print(" " * (n - row) + "*" + " *" * (row - 1))
    row -= 1
