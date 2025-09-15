n = int(input())

i = 0

while i <= n:
    if i == 0:

        space_count = 0
        while space_count <= n:

            print(" ", end="")
            space_count += 1

        print("|")

    else:

        space_count = 0
        while space_count < n - i:

            print(" ", end="")
            space_count += 1

        stars_count = 0
        while stars_count < i:

            print("*", end="")
            stars_count += 1

        print(" | ", end="")

        stars_count = 0
        while stars_count < i:

            print("*", end="")
            stars_count += 1

        print()

    i += 1
