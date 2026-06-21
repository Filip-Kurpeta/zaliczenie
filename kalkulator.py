def wyswietl_menu():
    print("\n--- KALKULATOR ---")
    print("1. Dodawanie (+)")
    print("2. Odejmowanie (-)")
    print("3. Mnozenie (*)")
    print("4. Dzielenie (/)")
    print("5. Potegowanie (^)")
    print("0. Wyjscie")


def main():
    while True:
        wyswietl_menu()

        try:
            wybor = int(input("Wybierz opcje: "))
        except ValueError:
            print("Blad wejscia! Koniec programu.")
            break

        if wybor == 0:
            print("Koniec programu. Do widzenia!")
            break

        if 1 <= wybor <= 5:
            try:
                liczba1 = float(input("Podaj pierwsza liczbe: "))
                liczba2 = float(input("Podaj druga liczbe: "))
            except ValueError:
                print("Blad wejscia! Koniec programu.")
                break

            if wybor == 1:
                wynik = liczba1 + liczba2
                print(f"\n=> Wynik: {liczba1:.2f} + {liczba2:.2f} = {wynik:.2f}")
            elif wybor == 2:
                wynik = liczba1 - liczba2
                print(f"\n=> Wynik: {liczba1:.2f} - {liczba2:.2f} = {wynik:.2f}")
            elif wybor == 3:
                wynik = liczba1 * liczba2
                print(f"\n=> Wynik: {liczba1:.2f} * {liczba2:.2f} = {wynik:.2f}")
            elif wybor == 4:
                if liczba2 == 0:
                    print("\n=> Blad: Nie mozna dzielic przez zero!")
                else:
                    wynik = liczba1 / liczba2
                    print(f"\n=> Wynik: {liczba1:.2f} / {liczba2:.2f} = {wynik:.2f}")
            elif wybor == 5:
                wynik = liczba1 ** liczba2
                print(f"\n=> Wynik: {liczba1:.2f} do potegi {liczba2:.2f} = {wynik:.2f}")
        else:
            print("\n=> Nieprawidlowy wybor! Sprobuj ponownie.")


if __name__ == "__main__":
    main()