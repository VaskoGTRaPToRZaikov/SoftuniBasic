start = int(input())
end = int(input())


start1 = start // 1000
start2 = (start // 100) % 10
start3 = (start // 10) % 10
start4 = start % 10

end1 = end // 1000
end2 = (end // 100) % 10
end3 = (end // 10) % 10
end4 = end % 10


number1 = start1
while number1 <= end1:

    if number1 % 2 == 1:

        number2 = start2
        while number2 <= end2:

            if number2 % 2 == 1:

                number3 = start3
                while number3 <= end3:

                    if number3 % 2 == 1:

                        number4 = start4
                        while number4 <= end4:

                            if number4 % 2 == 1:

                                number = number1 * 1000 + number2 * 100 + number3 * 10 + number4
                                print(number, end=' ')

                            number4 += 1

                    number3 += 1

            number2 += 1

    number1 += 1
