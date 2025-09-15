favorite_book = input()

count_books = 0

while True:
    checked_book = input()

    if checked_book == "No More Books":
        print(f"The book you search is not here!\nYou checked {count_books} books.")
        break
    else:

        if checked_book == favorite_book:
            print(f"You checked {count_books} books and found it.")
            break

        else:
            count_books += 1





