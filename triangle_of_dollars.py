# n = int(input())
#
# i = 1
#
# while i < n + 1:
#     symbol = "$ "
#
#     print(symbol * i)
#     i += 1

n = int(input())

row = 1

while row <= n:

    col = 1
    while col <= row:
        print("$ ", end="")
        col += 1

    print()
    row += 1