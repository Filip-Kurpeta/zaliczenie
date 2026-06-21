print("Dzialania na slowach")
print("Wpisz pusty tekst, aby zakonczyc program.\n")

while True:

    text = input("Podaj tekst: ")


    if text == "":
        break

    print(f"Tekst oryginalny: {text}")


    male_litery = text.lower()
    print(f"Male litery: {male_litery}")

    duze_litery = text.upper()
    print(f"Duze litery: {duze_litery}")


    dlugosc = len(text)
    print(f"Dlugosc tekstu: {dlugosc}")

    print("------------------------------")