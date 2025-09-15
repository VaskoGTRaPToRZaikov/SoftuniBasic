BTC_PRICE = 1168
CHINESE_UAN_PRICE = 0.15
DOLLAR_PRICE = 1.76
EURO_PRICE = 1.95

btc_number = int(input())
chinese_uan_number = float(input())
commission = float(input()) / 100

btc_sum = btc_number * BTC_PRICE

uan_sum = chinese_uan_number * CHINESE_UAN_PRICE

uan_sum_in_bgn = uan_sum * DOLLAR_PRICE

euro_sum = (btc_sum + uan_sum_in_bgn) / EURO_PRICE

result = euro_sum - (euro_sum * commission)

print(f"{result:.2f}")
