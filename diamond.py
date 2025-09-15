n = int(input())

if n == 1:
    print("*")

elif n % 2 == 0:

    for i in range (n // 2):
        left_dashes = "-" * (n // 2 - i - 1)
        middle_dashes = "-" * (i * 2)
        print(f"{left_dashes}*{middle_dashes}*{left_dashes}")

    for i in range(n // 2 - 2, -1, -1):
        left_dashes = "-" * (n // 2 - i - 1)
        middle_dashes = "-" * (i * 2)
        print(f"{left_dashes}*{middle_dashes}*{left_dashes}")

else:
    print(f"{'-' * ((n - 1) // 2)}*{'-' * ((n - 1) // 2)}")

    for i in range(1, n // 2):
        left_dashes = "-" * ((n - 1) // 2 - i)
        middle_dashes = "-" * (i * 2 - 1)
        print(f"{left_dashes}*{middle_dashes}*{left_dashes}")

    for i in range(n // 2, 0, -1):
        left_dashes = "-" * ((n - 1) // 2 - i)
        middle_dashes = "-" * (i * 2 - 1)
        print(f"{left_dashes}*{middle_dashes}*{left_dashes}")

    print(f"{'-' * ((n - 1) // 2)}*{'-' * ((n - 1) // 2)}")
