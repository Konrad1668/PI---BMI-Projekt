import csv

pola = []
wiersze = []

with open("danewejściowe.txt", "w") as plikCSV:
    czytnikCSV = csv.reader(plikCSV, delimiter=';')

    pola = next(czytnikCSV)

    for wiersz in czytnikCSV:
     wiersze.append(wiersz)


for wiersz in wiersze:
    iloczyn = float(wiersz[1])
    kwadrat = iloczyn**2


for wiersz in wiersze:
    iloraz = float(wiersz[0])
    bmi = iloraz/kwadrat
    print("BMI wynosi: ""%.2f " %bmi)

    file = open("bmi.txt", "a+")
    file.write(f"{bmi}")
    file.close()


