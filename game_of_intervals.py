moves = int(input())

result = 0

zero_nine = 0
ten_nineteen = 0
twenty_twenty_nine = 0
thirty_thirty_nine = 0
forty_fifty = 0
invalid_numbers = 0

for _ in range(moves):
    nums = int(input())

    if 0 <= nums <= 9:
        zero_nine += 1
        result += nums * 0.20

    elif 10 <= nums < 20:
        ten_nineteen += 1
        result += nums * 0.30

    elif 20 <= nums < 30:
        twenty_twenty_nine += 1
        result += nums * 0.40

    elif 30 <= nums < 40:
        thirty_thirty_nine += 1
        result += 50

    elif 40 <= nums <= 50:
        forty_fifty += 1
        result += 100

    else:
        invalid_numbers += 1
        result = result / 2

percent_zero_nine = zero_nine / moves * 100
percent_ten_nineteen = ten_nineteen / moves * 100
percent_twenty_twenty_nine = twenty_twenty_nine / moves * 100
percent_thirty_thirty_nine = thirty_thirty_nine / moves * 100
percent_forty_fifty = forty_fifty / moves * 100
percent_invalid_numbers = invalid_numbers / moves * 100

print(f"{result:.2f}")
print(f"From 0 to 9: {percent_zero_nine:.2f}%")
print(f"From 10 to 19: {percent_ten_nineteen:.2f}%")
print(f"From 20 to 29: {percent_twenty_twenty_nine:.2f}%")
print(f"From 30 to 39: {percent_thirty_thirty_nine:.2f}%")
print(f"From 40 to 50: {percent_forty_fifty:.2f}%")
print(f"Invalid numbers: {percent_invalid_numbers:.2f}%")
