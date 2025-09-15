number_students = int(input())

count_under_three = 0
count_between_three_four = 0
count_between_four_five = 0
count_more_than_five = 0
average_grades = 0

for _ in range(number_students):
    grades = float(input())

    average_grades += grades

    if 2 <= grades < 3:
        count_under_three += 1

    elif 3 <= grades < 4:
        count_between_three_four += 1

    elif 4 <= grades < 5:
        count_between_four_five += 1

    elif grades >= 5:
        count_more_than_five += 1

percent_failed = count_under_three / number_students * 100
percent_average = count_between_three_four / number_students * 100
percent_good = count_between_four_five / number_students * 100
percent_excellent = count_more_than_five / number_students * 100
average_success = average_grades / number_students

print(f"Top students: {percent_excellent:.2f}%")
print(f"Between 4.00 and 4.99: {percent_good:.2f}%")
print(f"Between 3.00 and 3.99: {percent_average:.2f}%")
print(f"Fail: {percent_failed:.2f}%")
print(f"Average: {average_success:.2f}")
