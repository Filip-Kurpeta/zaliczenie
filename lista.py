SIZE = 10


def print_array(arr):
    for i in range(len(arr)):
        print(f"numbers[{i}] = {arr[i]}")


def main():
    numbers = [1, 2, 3, -4, 50, 6, 7, 8, 9, 10]

    print("Original array:")
    print_array(numbers)


    sum_val = 0
    min_idx = 0
    max_idx = 0


   

    for i in range(SIZE):
        sum_val += numbers[i]
        if numbers[i] < numbers[min_idx]:
            min_idx = i
        if numbers[i] > numbers[max_idx]:
            max_idx = i

    print(f"\nMaximum: {numbers[max_idx]}")
    print(f"Minimum: {numbers[min_idx]}")
    print(f"Sum: {sum_val}")
    print(f"Average: {sum_val / SIZE:.2f}")


    numbers[min_idx], numbers[max_idx] = numbers[max_idx], numbers[min_idx]

    print("\nArray after swapping minimum and maximum:")
    print_array(numbers)


    sorted_arr = numbers.copy()

    #
    for i in range(SIZE - 1):
        for j in range(SIZE - 1 - i):
            if sorted_arr[j] > sorted_arr[j + 1]:

                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]

    print("\nSorted array:")
    print_array(sorted_arr)

    if SIZE % 2 == 0:
        median = (sorted_arr[SIZE // 2 - 1] + sorted_arr[SIZE // 2]) / 2.0
    else:
        median = sorted_arr[SIZE // 2]

    print(f"\nMedian: {median:.2f}")

if __name__ == "__main__":
    main()