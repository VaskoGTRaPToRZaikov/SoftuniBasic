strawberry_price = float(input())
quantity_bananas = float(input())
quantity_oranges = float(input())
quantity_raspberry = float(input())
quantity_strawberry = float(input())

raspberry_price = strawberry_price * 0.50
orange_price = raspberry_price * 0.60
banana_price = raspberry_price * 0.20


final_sum = (quantity_strawberry * strawberry_price
             + quantity_bananas * banana_price + quantity_oranges * orange_price
             + quantity_raspberry * raspberry_price)

print(f"{final_sum:.2f}")

