#include <stdio.h>
#include <math.h>

void wyswietlMenu() {
    printf("\n--- KALKULATOR ---\n");
    printf("1. Dodawanie (+)\n");
    printf("2. Odejmowanie (-)\n");
    printf("3. Mnozenie (*)\n");
    printf("4. Dzielenie (/)\n");
    printf("5. Potegowanie (^)\n");
    printf("0. Wyjscie\n");
    printf("Wybierz opcje: ");
}

int main() {
    int wybor;
    double liczba1, liczba2, wynik;


    while (1) {
        wyswietlMenu();


        if (scanf("%d", &wybor) != 1) {
            printf("Blad wejscia! Koniec programu.\n");
            break;
        }


        if (wybor == 0) {
            printf("Koniec programu. Do widzenia!\n");
            break;
        }


        if (wybor >= 1 && wybor <= 5) {
            printf("Podaj pierwsza liczbe: ");
            scanf("%lf", &liczba1);
            printf("Podaj druga liczbe: ");
            scanf("%lf", &liczba2);


            switch (wybor) {
                case 1:
                    wynik = liczba1 + liczba2;
                    printf("\n=> Wynik: %.2lf + %.2lf = %.2lf\n", liczba1, liczba2, wynik);
                    break;
                case 2:
                    wynik = liczba1 - liczba2;
                    printf("\n=> Wynik: %.2lf - %.2lf = %.2lf\n", liczba1, liczba2, wynik);
                    break;
                case 3:
                    wynik = liczba1 * liczba2;
                    printf("\n=> Wynik: %.2lf * %.2lf = %.2lf\n", liczba1, liczba2, wynik);
                    break;
                case 4:
                    if (liczba2 == 0) {
                        printf("\n=> Blad: Nie mozna dzielic przez zero!\n");
                    } else {
                        wynik = liczba1 / liczba2;
                        printf("\n=> Wynik: %.2lf / %.2lf = %.2lf\n", liczba1, liczba2, wynik);
                    }
                    break;
                case 5:
                    wynik = pow(liczba1, liczba2);
                    printf("\n=> Wynik: %.2lf do potegi %.2lf = %.2lf\n", liczba1, liczba2, wynik);
                    break;
            }
        } else {
            printf("\n=> Nieprawidlowy wybor! Sprobuj ponownie.\n");
        }
    }

    return 0;
}