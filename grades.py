number_students = int(input())

count_c_grades = 0
count_b_grades = 0
count_a_grades = 0
count_s_grades = 0
grades_sum = 0

for _ in range(number_students):
    grades = float(input())
    grades_sum += grades

    if 2.00 <= grades < 3.00:
        count_c_grades += 1
    elif 3.00 <= grades < 4.00:
        count_b_grades += 1
    elif 4.00 <= grades < 5.00:
        count_a_grades += 1
    elif 5.00 <= grades <= 6.00:
        count_s_grades += 1

average_grade = grades_sum / number_students

percent_c_grades = count_c_grades / number_students * 100
percent_b_grades = count_b_grades / number_students * 100
percent_a_grades = count_a_grades / number_students * 100
percent_s_grades = count_s_grades / number_students * 100

print(f"Top students: {percent_s_grades:.2f}%")
print(f"Between 4.00 and 4.99: {percent_a_grades:.2f}%")
print(f"Between 3.00 and 3.99: {percent_b_grades:.2f}%")
print(f"Fail: {percent_c_grades:.2f}%")
print(f"Average: {average_grade:.2f}")