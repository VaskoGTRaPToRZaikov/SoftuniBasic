BASKET_PRICE = 1.50
WREATH_PRICE = 3.80
CHOCO_BUNNY_PRICE = 7

clients = int(input())
n = 0
overall_sum = 0

while n < clients:
    finish_purchase = False
    final_sum = 0
    product_count = 0
    n += 1

    while not finish_purchase:
        product = input()

        if product == "Finish":
            finish_purchase = True
            if product_count % 2 == 0:
                final_sum *= 0.80
            overall_sum += final_sum
            print(f"You purchased {product_count} items for {final_sum:.2f} leva.")
            product_count = 0
            final_sum = 0
            break

        if product == "basket":
            final_sum += BASKET_PRICE
            product_count += 1

        elif product == "wreath":
            final_sum += WREATH_PRICE
            product_count += 1

        elif product == "chocolate bunny":
            final_sum += CHOCO_BUNNY_PRICE
            product_count += 1


average_client_sum = overall_sum / clients

print(f"Average bill per client is: {average_client_sum:.2f} leva.")