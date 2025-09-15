Yearly_expenses = 12000
ODD_BONUS_TAX = 50

inheritance = float(input())
year_up_to_live = int(input())

number_years = year_up_to_live - 1800
age = 18

even_expenses = 0
odd_expenses = 0

for i in range(number_years + 1):
    if i % 2 == 0:
        even_expenses += 12000
        age += 1
    else:
        odd_expenses += 12000 + (50 * age)
        age += 1

total_expenses = even_expenses + odd_expenses

if inheritance >= total_expenses:
    print(f"Yes! He will live a carefree life and will have {inheritance - total_expenses:.2f} dollars left.")
else:
    print(f"He will need {total_expenses - inheritance:.2f} dollars to survive.")