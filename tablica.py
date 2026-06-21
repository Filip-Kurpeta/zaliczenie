import statistics


def menu():
    print("\n1. Wpisz nowe wartosci do tablicy")
    print("2. Wyswietl zawartosc tablicy")
    print("3. Znajdz wartosc minimalna")
    print("4. Znajdz wartosc maksymalna")
    print("5. Oblicz wartosc srednia")
    print("6. Posortuj tablice (Wbudowane sortowanie pythona)")
    print("7. Oblicz mediane")
    print("0. WYJSCIE")
    return input("Wybierz opcje: ")


def main():
    
    SIZE = 10
    array = [1, 2, 3, -4, 50, 6, 7, 8, 9, 10]

    print("--- PROSTA TABLICA ---")

    while True:
        option = menu()

        if option == '0':
            break

        elif option == '1':
            print(f"\nWprowadz {SIZE} nowych wartosci:")
            array = []
            for i in range(SIZE):
                val = int(input(f"array[{i}] = "))
                array.append(val)

        elif option == '2':
            print("\nZawartosc tablicy:")
            for i, val in enumerate(array):
                print(f"array[{i}] = {val}")

        elif option == '3':
            print(f"\nMinimalna wartosc: {min(array)}")

        elif option == '4':
            print(f"\nMaksymalna wartosc: {max(array)}")

        elif option == '5':
            srednia = sum(array) / len(array)
            print(f"\nSrednia wartosc: {srednia:.2f}")

        elif option == '6':
            array.sort()
            print("\nTablica zostala posortowana!")
            for i, val in enumerate(array):
                print(f"array[{i}] = {val}")

        elif option == '7':
            mediana = statistics.median(array)
            print(f"\nMediana wynosi: {mediana:.2f}")

        else:
            print("\nWybierz poprawna opcje...")

    print("\nKONIEC PROGRAMU!")


if __name__ == "__main__":
    main()