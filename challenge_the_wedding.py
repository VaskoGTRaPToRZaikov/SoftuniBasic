males = int(input())
females = int(input())
max_tables = int(input())

count_occupied_tables = 0

for man in range(1, males + 1):
    for woman in range(1, females + 1):

        if count_occupied_tables >= max_tables:
            break

        print(f"({man} <-> {woman})", end=" ")
        count_occupied_tables += 1