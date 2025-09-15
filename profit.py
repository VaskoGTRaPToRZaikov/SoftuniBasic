one_leva_coins = int(input())
two_leva_coins = int(input())
five_leva_banknotes = int(input())

target_sum = int(input())

for one_leva in range(one_leva_coins + 1):
    for two_leva in range(two_leva_coins + 1):
        for five_leva in range(five_leva_banknotes + 1):

            current_sum = one_leva * 1 + two_leva * 2 + five_leva * 5

            if current_sum == target_sum:
                print(f"{one_leva} * 1 lv. + {two_leva} * 2 lv. + {five_leva} * 5 lv. = {target_sum} lv.")