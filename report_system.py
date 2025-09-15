expected_sum = int(input())

enough_sum = True
count_objects = 0
cash_sum = 0
card_sum = 0
current_sum = 0
cash_count = 0
card_count = 0

while current_sum < expected_sum:
    command = input()

    if command == "End":
        enough_sum = False
        break

    else:
        object_price = int(command)
        count_objects += 1

        if count_objects % 2 == 0:

            if object_price >= 10:
                print("Product sold!")
                card_sum += object_price
                card_count += 1
                current_sum += object_price

            else:
                print("Error in transaction!")

        else:
            if object_price <= 100:
                print("Product sold!")
                cash_sum += object_price
                cash_count += 1
                current_sum += object_price

            else:
                print("Error in transaction!")

if cash_count > 0:
    average_cash = cash_sum / cash_count

else:
    average_cash = 0

if card_count > 0:
    average_card = card_sum / card_count

else:
    average_card = 0

if enough_sum:
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_card:.2f}")

else:
    print(f"Failed to collect required money for charity.")