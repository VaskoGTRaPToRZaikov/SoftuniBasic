balance = 0

while True:
    text = input()

    if text == "NoMoreMoney":
        break

    else:
        increase = float(text)

        if increase >= 0:
            print(f"Increase: {increase:.2f}")
            balance += increase

        else:
            print("Invalid operation!")
            break

print(f"Total: {balance:.2f}")

