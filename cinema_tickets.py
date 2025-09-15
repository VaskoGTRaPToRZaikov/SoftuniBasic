student_tickets = 0
standard_tickets = 0
kids_tickets = 0
overall_tickets = 0

while True:
    movie_name = input()

    if movie_name == "Finish":
        break

    capacity = int(input())
    tickets = 0


    while tickets < capacity:
        ticket_type = input()

        if ticket_type == "End":
            break

        tickets += 1
        overall_tickets += 1

        if ticket_type == "student":
            student_tickets += 1

        elif ticket_type == "standard":
            standard_tickets += 1

        elif ticket_type == "kid":
            kids_tickets += 1

    occupancy_rate = tickets / capacity * 100
    print(f"{movie_name} - {occupancy_rate:.2f}% full.")
    tickets = 0

percent_student_tickets = student_tickets / overall_tickets * 100
percent_standard_tickets = standard_tickets / overall_tickets * 100
percent_kids_tickets = kids_tickets / overall_tickets * 100

print(f"Total tickets: {overall_tickets}\n{percent_student_tickets:.2f}% student tickets.\n"
      f"{percent_standard_tickets:.2f}% standard tickets.\n{percent_kids_tickets:.2f}% kids tickets.")
