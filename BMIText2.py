import csv

pola = []
wiersze = []

with open(r'C:\Users\Default User\Desktop\danewejsciowe.csv') as plikCSV:
    czytnikCSV = csv.reader(plikCSV, delimiter=';')

    pola = next(czytnikCSV)

    for wiersz in czytnikCSV:
     wiersze.append(wiersz)


for wiersz in wiersze:
    iloczyn = float(wiersz[1])
    kwadrat = iloczyn**2
    iloraz = float(wiersz[0])
    bmi = round(iloraz/kwadrat, 2)

if bmi < 16:
    

    file = open("bmi.txt", "a+")
    file.write(f"{bmi}\n", n)
    file.close()
