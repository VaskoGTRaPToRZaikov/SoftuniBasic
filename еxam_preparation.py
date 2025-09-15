possible_bad_grades = int(input())

overall_score = 0
solved_problems = 0
last_task = 0
count_bad_grades = 0
has_failed = True

while count_bad_grades < possible_bad_grades:
    task_name = input()

    if task_name == "Enough":
        has_failed = False
        break

    else:
        grades = int(input())
        if grades <= 4:
            count_bad_grades += 1
        last_task = task_name
        overall_score += grades
        solved_problems += 1



average_score = overall_score / solved_problems

if has_failed:
    print(f"You need a break, {count_bad_grades} poor grades.")

else:
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {solved_problems}")
    print(f"Last problem: {last_task}")

