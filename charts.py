import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

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
df1 = pd.read_csv("bmi.csv", sep=" ", header=None, names=["Waga", "Wzrost", "BMI", "status"])
df2 = pd.read_csv("results.txt", sep=" ", header=None, names=["Waga", "Wzrost", "BMI", "status"])
df = pd.concat([df1, df2]).reset_index(drop=True)

'''Wprowadzenie danych z df na układ współrzędnych'''
sns.relplot(data=df, x="Wzrost", y="Waga", hue="status", palette=paleta)
plt.title('Body Mass Index')
plt.show()
