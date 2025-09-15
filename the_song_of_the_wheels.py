number = int(input())

password_count = 0
password = ""
has_password = False

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):

                if a < b and c > d:

                    if a * b + c * d == number:
                        print(f"{a}{b}{c}{d}", end=" ")
                        password_count += 1

                        if password_count == 4:
                            password = str(f"{a}{b}{c}{d}")
                            has_password = True

print()

if has_password:
    print(f"Password: {password}")

else:
    print("No!")