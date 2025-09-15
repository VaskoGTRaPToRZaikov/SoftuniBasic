# LITERS_PAINT_PER_SQUARE_METER = 1

height = int(input())
width = int(input())
percent_not_painting = int(input()) / 100

area = (height * width) * 4
painting_area = round(area - (area * percent_not_painting))
left_painting_area = painting_area

while True:
    liters_paint = input()

    if liters_paint == "Tired!":
        print(f"{left_painting_area} quadratic m left.")
        break

    else:
        if left_painting_area == int(liters_paint):
            print(f"All walls are painted! Great job, Pesho!")
            break
        elif left_painting_area < int(liters_paint):
            print(f"All walls are painted and you have {int(liters_paint) - left_painting_area} l paint left!")
            break
        else:
            left_painting_area -= int(liters_paint)

