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