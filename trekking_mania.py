n = int(input())

count_musala = 0
count_montblanc = 0
count_kilimanjaro = 0
count_k2 = 0
count_everest = 0

overall_people = 0

for _ in range(n):
    peoples = int(input())
    overall_people += peoples

    if 0 < peoples <= 5:
        count_musala += peoples

    elif 5 < peoples <= 12:
        count_montblanc += peoples

    elif 12 < peoples <= 25:
        count_kilimanjaro += peoples

    elif 25 < peoples <= 40:
        count_k2 += peoples

    elif 40 < peoples:
        count_everest += peoples

percent_musala = count_musala / overall_people * 100
percent_montblanc = count_montblanc / overall_people * 100
percent_kilimanjaro = count_kilimanjaro / overall_people * 100
percent_k2 = count_k2 / overall_people * 100
percent_everest = count_everest / overall_people * 100

print(f"{percent_musala:.2f}%")
print(f"{percent_montblanc:.2f}%")
print(f"{percent_kilimanjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")