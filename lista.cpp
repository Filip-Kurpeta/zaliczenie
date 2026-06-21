#include <stdio.h>

#define SIZE 10


void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("numbers[%d] = %d\n", i, arr[i]);
    }
}

int main() {
    int numbers[SIZE] = {1, 2, 3, -4, 50, 6, 7, 8, 9, 10};
    int sorted[SIZE];
    int sum = 0, minIdx = 0, maxIdx = 0;

    printf("Original array:\n");
    printArray(numbers, SIZE);


    for (int i = 0; i < SIZE; i++) {
        sum += numbers[i];
        if (numbers[i] < numbers[minIdx]) minIdx = i;
        if (numbers[i] > numbers[maxIdx]) maxIdx = i;
    }

    printf("\nMaximum: %d\n", numbers[maxIdx]);
    printf("Minimum: %d\n", numbers[minIdx]);
    printf("Sum: %d\n", sum);
    printf("Average: %.2f\n", (float)sum / SIZE);


    int temp = numbers[minIdx];
    numbers[minIdx] = numbers[maxIdx];
    numbers[maxIdx] = temp;

    printf("\nArray after swapping minimum and maximum:\n");
    printArray(numbers, SIZE);


    for (int i = 0; i < SIZE; i++) {
        sorted[i] = numbers[i];
    }


    for (int i = 0; i < SIZE - 1; i++) {
        for (int j = 0; j < SIZE - 1 - i; j++) {
            if (sorted[j] > sorted[j + 1]) {
                temp = sorted[j];
                sorted[j] = sorted[j + 1];
                sorted[j + 1] = temp;
            }
        }
    }

    printf("\nSorted array:\n");
    printArray(sorted, SIZE);


    float median = (SIZE % 2 == 0)
        ? (sorted[SIZE / 2 - 1] + sorted[SIZE / 2]) / 2.0
        : sorted[SIZE / 2];

    printf("\nMedian: %.2f\n", median);

    return 0;
}