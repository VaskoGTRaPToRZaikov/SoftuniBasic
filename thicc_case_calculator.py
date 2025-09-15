MOONSHINE = 225000
WHISKEY = 40000
VODKA = 35000
DEFIB = 235000
LEDX = 725000
IBUPROFEN = 150000
TOOTHPASTE = 100000

number_moonshine = 50
number_whiskey = 30
number_vodka = 50
number_defib = 15
number_ledx = 15
number_ibuprofen = 15
number_toothpaste = 15

thicc_case_price1 = number_moonshine * MOONSHINE + number_whiskey * WHISKEY + number_vodka * VODKA

thicc_case_price2 = (number_ledx * LEDX + number_defib * DEFIB
                     + number_ibuprofen * IBUPROFEN + number_toothpaste * TOOTHPASTE)

print(thicc_case_price1)
print(thicc_case_price2)
