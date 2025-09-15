start_letter = input()
end_letter = input()
skip_letter = input()

count = 0

for first in range(ord(start_letter), ord(end_letter) + 1):
    for second in range(ord(start_letter), ord(end_letter) + 1):
        for third in range(ord(start_letter), ord(end_letter) + 1):

            first_char = chr(first)
            second_char = chr(second)
            third_char = chr(third)

            if first_char != skip_letter and second_char != skip_letter and third_char != skip_letter:

                print(f"{first_char}{second_char}{third_char}", end=" ")
                count += 1

print(count)