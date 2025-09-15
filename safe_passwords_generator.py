number1 = int(input())
number2 = int(input())
max_passwords = int(input())

password_count = 0

char_a = 35
char_b = 64

for x in range(1, number1 + 1):
    for y in range(1, number2 + 1):

        if password_count >= max_passwords:
            break

        a = chr(char_a)
        b = chr(char_b)

        print(f"{a}{b}{x}{y}{b}{a}", end="|")
        char_a += 1
        char_b += 1
        password_count += 1

        if char_a > 55:
            char_a = 35

        if char_b > 96:
            char_b = 64
