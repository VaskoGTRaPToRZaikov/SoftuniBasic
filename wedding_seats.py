end_sector = input()
first_sector_rows = int(input())
odd_row_seats = int(input())
even_row_seats = odd_row_seats + 2

rows = first_sector_rows
total_seats = 0

for sector in range(ord("A"), ord(end_sector) + 1):
    for row in range(1, rows + 1):
        if row % 2 == 0:
            seats = even_row_seats

        else:
            seats = odd_row_seats

        for seat in range(seats):

            print(f"{chr(sector)}{row}{chr(97 + seat)}")
            total_seats += 1
    rows += 1

print(total_seats)

