days = int(input())
initial_medics = 7

medics = initial_medics
unexamined_patients = 0
patients_examined = 0

for i in range(1,days + 1):
    patients = int(input())
    if i % 3 == 0:
        if unexamined_patients > patients_examined:
            medics += 1
    if medics >= patients:
        patients_examined += patients
    if medics < patients:
        patients_examined += medics
        unexamined_patients += patients - medics



print(f"Treated patients: {patients_examined}.")
print(f"Untreated patients: {unexamined_patients}.")

