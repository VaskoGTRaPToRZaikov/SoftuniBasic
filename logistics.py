MICROBUS_PRICE = 200
TRUCK_PRICE = 175
TRAIN_PRICE = 120

n = int(input())

microbus_cargo = 0
truck_cargo = 0
train_cargo = 0
overall_cargo = 0

for _ in range(n):
    cargo = int(input())
    overall_cargo += cargo

    if cargo < 4:
        microbus_cargo += cargo
    elif 4 <= cargo < 12:
        truck_cargo += cargo
    else:
        train_cargo += cargo

average_price = ((microbus_cargo * MICROBUS_PRICE) + (truck_cargo * TRUCK_PRICE)
                 + (train_cargo * TRAIN_PRICE)) / overall_cargo

percent_microbus = microbus_cargo / overall_cargo * 100
percent_truck = truck_cargo / overall_cargo * 100
percent_train = train_cargo / overall_cargo * 100

print(f"{average_price:.2f}")
print(f"{percent_microbus:.2f}%")
print(f"{percent_truck:.2f}%")
print(f"{percent_train:.2f}%")