import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

'''Przyporządkowanie kolorów Hex do poszczególnych zakresów z BMI:
        Wg - Wygłodzenie
        Wy - Wychudzenie
        Ni - Niedowaga
        P - Pożądana masa ciała
        Na - Nadwaga
        OI - Otyłość I stopnia
        OII - Otyłość II stopnia
        OIII - Otyłość III stopnia'''
paleta = {
    'Wg': '#222280',
    'Wy': '#267CEC',
    'Ni': '#69FFA1',
    'P': '#CAFA81',
    'Na': '#EFFF8C',
    'OI': '#F9F948',
    'OII': '#FF370E',
    'OIII': '#661303'
}
'''Styl układu współrzędnych'''
sns.set_style("darkgrid", {"axes.facecolor": ".8"})

'''Funkcja df1 i df2 zczytujące dane z plików tekstowych, porządkujące kolumny dokumentów według wzoru - WAGA, WZROST, 
WYNIK BMI LICZBOWY, SKRÓT NAZWY ZAKRESU UŻYTY W PALECIE (np. Wg). Funkcja df łączy dane z obu plików w jeden zestaw'''
df1 = pd.read_csv("file.txt", sep=" ", header=None, names=["Waga", "Wzrost", "BMI", "status"])
df2 = pd.read_csv("file2.txt", sep=" ", header=None, names=["Waga", "Wzrost", "BMI", "status"])
df = pd.concat([df1, df2]).reset_index(drop=True)

'''Wprowadzenie danych z df na układ współrzędnych'''
sns.relplot(data=df, x="Wzrost", y="Waga", hue="status", palette=paleta)
plt.title('Body Mass Index')
plt.show()
