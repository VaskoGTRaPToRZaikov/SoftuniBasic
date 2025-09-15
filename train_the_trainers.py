number_jurors = int(input())

sum_average_grade = 0
presentation_count = 0

while True:
    presentation = input()


    if presentation == "Finish":
        break

    presentation_count += 1

    sum_grades = 0

    for _ in range(number_jurors):
        grades = float(input())
        sum_grades += grades

    average_grade = sum_grades / number_jurors
    sum_average_grade += average_grade

    print(f"{presentation} - {average_grade:.2f}.")

    average_grade = 0
    sum_grades = 0

overall_average_grade = sum_average_grade / presentation_count

print(f"Student's final assessment is {overall_average_grade:.2f}.")



