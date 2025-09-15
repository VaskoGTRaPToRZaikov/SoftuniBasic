n = int(input())

result = 0

i = 0

while i < n:
    num = int(input())
    result += num
    i += 1

average_number = result / n

print(f"{average_number:.2f}")
