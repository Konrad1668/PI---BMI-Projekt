import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import csv

pola = []
wiersze = []

with open(r'C:\Users\Konrad\Desktop\danewejsciowe.csv') as plikCSV:
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
    file.write(f"{float(wiersz[1])};{float(wiersz[0])};{bmi};{status}\n")
    file.close()

def BMI():
    with open("results.txt", "w") as f:
        print("Wybierz jednostkę. Dla jednostek metrycznych wybierz 0 dla impierialnych wybierz 1: ")
        d = int(input())
        while d != 0 and d != 1:
            print("Podaj prawdiłową liczbę")
            d = int(input())
        print("Podaj ilość wprowadzanych pomiarów: ")
        howmany = int(input())
        while howmany < 0:
            print("Wprowadź liczbę większą od zera: ")
            howmany = int(input())
        for i in range (0, howmany):
            if d == 0:
                print("Wpisz swoją wagę w kg: ")
                a = float(input())
                while a < 0:
                    print("Waga nie może być ujemna")
                    a = float(input())
                f.write(str(a) + " ")
                print("Wpisz swój wzrost w m: ")
                b = float(input())
                while b < 0:
                    print("Wzrost nie może być ujemny")
                    b = float(input())
                f.write(str(b) + " ")
                formula = a / (b ** 2)
            else:
                print("Wpisz swoją wagę w funtach: ")
                a = float(input())
                while a < 0:
                    print("Waga nie może być ujemna")
                    a = float(input())
                f.write(str(a) + " ")
                print("Wpisz swój wzrost w calach: ")
                b = float(input())
                while b < 0:
                    print("Wzrost nie może być mniejszy od 0")
                    b = float(input())
                f.write(str(b) + " ")
                formula = (a / b ** 2) * 703

            f.write(str(formula) + " ")
            print("BMI = ", formula)
            if formula < 16:
                f.write("WYGLODZENIE\n")
                print("BMI wskazuje na wygłodzenie")
            elif 16 <= formula <= 16.99:
                f.write("WYCHUDZENIE\n")
                print("BMI wskazuje na wychudzenie")
            elif 17 <= formula <= 18.49:
                f.write("NIEDOWAGA\n")
                print("BMI wskazuje na niedowagę")
            elif 18.50 <= formula <= 24.99:
                f.write("NORMA\n")
                print("BMI jest w normie")
            elif 25 <= formula <= 29.99:
                f.write("NADWAGA\n")
                print("BMI wskazuje na nadwagę")
            elif 30 <= formula <= 34.99:
                f.write("OTYLOSC I STOPNIA\n")
                print("BMI wskazuje na otyłość I stopnia")
            elif 35 <= formula <= 39.99:
                f.write("OTYLOSC II STOPNIA\n")
                print("BMI wskazuje na otyłość II stopnia (duża)")
            else:
                f.write("OTYLOSC III STOPNIA\n")
                print("BMI wskazuje na otyłość III stopnia (choroba)")

BMI()

'''Przyporządkowanie kolorów Hex do poszczególnych zakresów z BMI'''
paleta = {
    'WYGLODZENIE': '#222280',
    'WYCHUDZENIE': '#267CEC',
    'NIEDOWAGA': '#69FFA1',
    'NORMA': '#CAFA81',
    'NADWAGA': '#EFFF8C',
    'OTYLOSC I STOPNIA': '#F9F948',
    'OTYLOSC II STOPNIA': '#FF370E',
    'OTYLOSC III STOPNIA': '#661303'
}
'''Styl układu współrzędnych'''
sns.set_style("darkgrid", {"axes.facecolor": ".8"})

'''Funkcja df1 i df2 zczytujące dane z plików tekstowych, porządkujące kolumny dokumentów według wzoru - WAGA, WZROST, 
WYNIK BMI LICZBOWY, SKRÓT NAZWY ZAKRESU UŻYTY W PALECIE (np. Wg). Funkcja df łączy dane z obu plików w jeden zestaw'''
df1= pd.read_csv("bmi.txt", sep=";", header=None, names=["Waga", "Wzrost", "BMI", "status"])
df2 = pd.read_csv("results.txt", sep=" ", header=None, names=["Waga", "Wzrost", "BMI", "status"])
df = pd.concat([df1,df2]).reset_index(drop=True)

'''Wprowadzenie danych z df na układ współrzędnych'''
sns.relplot(data=df, x="Wzrost", y="Waga", hue="status", palette=paleta)
plt.title('Body Mass Index')
plt.show()
