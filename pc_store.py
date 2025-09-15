USD_TO_BGN = 1.57

cpu_price = float(input())
gpu_price = float(input())
ram_price = float(input())
number_ram = int(input())
discount = float(input())

cpu_bgn_price = cpu_price * 1.57
gpu_bgn_price = gpu_price * 1.57
ram_bgn_price = ram_price * 1.57

final_cpu_price = cpu_bgn_price - (cpu_bgn_price * discount)
final_gpu_price = gpu_bgn_price - (gpu_bgn_price * discount)

overall_payment = final_cpu_price + final_gpu_price + (ram_bgn_price * number_ram)

print(f"Money needed - {overall_payment:.2f} leva.")