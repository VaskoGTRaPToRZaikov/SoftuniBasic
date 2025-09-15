# word = ""
#
# found_c = False
# found_o = False
# found_n = False
#
# while True:
#     symbol = input()
#
#     if symbol == "End":
#         break
#
#     if symbol.isalpha():
#
#         if symbol == "c":
#             if found_c == False:
#                 found_c = True
#             else:
#                 word = word + symbol
#
#         elif symbol == "o":
#             if found_o == False:
#                 found_o = True
#             else:
#                 word = word + symbol
#
#         elif symbol == "n":
#             if found_n == False:
#                 found_n = True
#             else:
#                 word = word + symbol
#
#         else:
#             word = word + symbol
#
#         if found_c == True and found_o == True and found_n == True:
#             print(word + " ", end="")
#
#             word = ""
#             found_c = False
#             found_o = False
#             found_n = False
#
#

word = ""

found_c = False
found_o = False
found_n = False

while True:
    symbol = input()

    if symbol == "End":
        break


    if symbol.isalpha():

        if symbol == "c":
            if not found_c:
                found_c = True
            else:
                word = word + symbol

        elif symbol == "o":
            if not found_o:
                found_o = True
            else:
                word = word + symbol

        elif symbol == "n":
            if not found_n:
                found_n = True
            else:
                word = word + symbol

        else:
            word = word + symbol

        if found_c == True and found_o == True and found_n == True:
            print(word + " ", end="")

            word = ""
            found_c = False
            found_o = False
            found_n = False

    else:
        continue