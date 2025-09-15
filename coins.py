instead = int(float(input()) * 100)

coins_count = 0

while instead > 0:
    coins_count += 1

    if instead >= 200:
        instead -= 200

    elif instead >= 100:
        instead -= 100

    elif instead >= 50:
        instead -= 50

    elif instead >= 20:
        instead -= 20

    elif instead >= 10:
        instead -= 10

    elif instead >= 5:
        instead -= 5

    elif instead >= 2:
        instead -= 2

    elif instead >= 1:
        instead -= 1

print(coins_count)
