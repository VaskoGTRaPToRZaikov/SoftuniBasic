n = int(input())

roof_rows = (n + 1) // 2

if n % 2 == 1:
    stars = 1

else:
    stars = 2

for i in range(roof_rows):
    space = (n - stars) // 2

    print("-" * space + "*" * stars + "-" * space)

    stars += 2

body_rows = n // 2

for o in range(body_rows):

    print("|" + "*" * (n - 2) + "|")

