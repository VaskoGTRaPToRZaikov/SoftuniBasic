name = input()

count_failed = 0
count_class = 0
grades_sum = 0
success_class = 0

while True:
    grades = float(input())

    if grades < 4:
        count_failed += 1

        if count_failed > 1:
            print(f"{name} has been excluded at {count_class} grade")
            break

        else:
            count_class += 1

    else:
        count_class += 1
        success_class += 1
        grades_sum += grades

    if success_class == 12:
        average_grades = grades_sum / success_class
        print(f"{name} graduated. Average grade: {average_grades:.2f}")
        break

