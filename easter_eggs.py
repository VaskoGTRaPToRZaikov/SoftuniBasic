n = int(input())

count_red = 0
count_orange = 0
count_blue = 0
count_green = 0

for _ in range(n):
    egg_color = input()

    if egg_color == "red":
        count_red += 1

    elif egg_color == "orange":
        count_orange += 1

    elif egg_color == "blue":
        count_blue += 1

    elif egg_color == "green":
        count_green += 1

max_color = ""
max_eggs = max(count_red, count_orange, count_blue, count_green)

if max_eggs == count_red:
    max_color = "red"

elif max_eggs == count_orange:
    max_color = "orange"

elif max_eggs == count_blue:
    max_color = "blue"

elif max_eggs == count_green:
    max_color = "green"

print(f"Red eggs: {count_red}")
print(f"Orange eggs: {count_orange}")
print(f"Blue eggs: {count_blue}")
print(f"Green eggs: {count_green}")
print(f"Max eggs: {max_eggs} -> {max_color}")