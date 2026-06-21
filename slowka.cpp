#include <stdio.h>
#include <string.h>

#define TEXT_SIZE 80

void toLower(char text[]) {
    for (int i = 0; text[i] != '\0'; i++) {
        if (text[i] >= 'A' && text[i] <= 'Z') {
            text[i] += ('a' - 'A');
        }
    }
}

void toUpper(char text[]) {
    for (int i = 0; text[i] != '\0'; i++) {
        if (text[i] >= 'a' && text[i] <= 'z') {
            text[i] -= ('a' - 'A');
        }
    }
}

int main() {
    char text[TEXT_SIZE];

    printf("Dzialania na slowach\n");
    printf("Wpisz pusty tekst, aby zakonczyc program.\n\n");

    while (1) {
        printf("Podaj tekst: ");
        fgets(text, TEXT_SIZE, stdin);


        text[strcspn(text, "\n")] = '\0';

        if (text[0] == '\0') {
            break;
        }

        printf("Tekst oryginalny: %s\n", text);

        toLower(text);
        printf("Male litery: %s\n", text);

        toUpper(text);
        printf("Duze litery: %s\n", text);


        printf("Dlugosc tekstu: %d\n", (int)strlen(text));
        printf("------------------------------\n");
    }

    return 0;
}