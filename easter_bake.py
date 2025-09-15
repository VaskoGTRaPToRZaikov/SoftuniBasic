import math

n = int(input())

max_sugar = 0
max_flour = 0

overall_sugar = 0
overall_flour = 0

for _ in range(n):
    quantity_sugar = int(input())
    quantity_flour = int(input())

    overall_sugar += quantity_sugar
    overall_flour += quantity_flour

    if quantity_sugar > max_sugar:
        max_sugar = quantity_sugar

    if quantity_flour > max_flour:
        max_flour = quantity_flour

sugar_packages = math.ceil(overall_sugar / 950)
flour_packages = math.ceil(overall_flour / 750)

print(f"Sugar: {sugar_packages}")
print(f"Flour: {flour_packages}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")