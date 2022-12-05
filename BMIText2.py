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
        status = "WYGLODZENIE"
    elif 16 <= bmi <= 16.99:
        status = "WYCHUDZENIE"
    elif 17 <= bmi <= 18.49:
        status = "NIEDOWAGA"
    elif 18.50 <= bmi <= 24.99:
        status = "NORMA"
    elif 25 <= bmi <= 29.99:
        status = "NADWAGA"
    elif 30 <= bmi <= 34.99:
        status = "OTYLOSC I STOPNIA"
    elif 35 <= bmi <= 39.99:
        status = "OTYLOSC II STOPNIA"
    else:
        status = "OTYLOSC III STOPNIA"

    file = open("bmi.txt", "a+")
    file.write(f"{float(wiersz[0])};{float(wiersz[1])};{bmi};{status}\n")
    file.close()
