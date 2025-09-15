WATER_TAX = 20
INTERNET_TAX = 15

months = int(input())

others_tax = 0

overall_water_tax = 0
overall_internet_tax = 0
overall_electricity_tax = 0
overall_others_tax = 0


for _ in range(months):
    electricity_tax = float(input())

    others_tax = (WATER_TAX + INTERNET_TAX + electricity_tax
                  + (WATER_TAX + INTERNET_TAX + electricity_tax) * 0.20)

    overall_water_tax += WATER_TAX
    overall_internet_tax += INTERNET_TAX
    overall_electricity_tax += electricity_tax
    overall_others_tax += others_tax

average_month_tax = (overall_water_tax + overall_internet_tax
                     + overall_electricity_tax + overall_others_tax) / months

print(f"Electricity: {overall_electricity_tax:.2f} lv")
print(f"Water: {overall_water_tax:.2f} lv")
print(f"Internet: {overall_internet_tax:.2f} lv")
print(f"Other: {overall_others_tax:.2f} lv")
print(f"Average: {average_month_tax:.2f} lv")

