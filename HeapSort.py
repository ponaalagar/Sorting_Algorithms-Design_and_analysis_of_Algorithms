# It is a sorting technique using a binary heap structure

def heapify(array: list, n: int, i: int):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] > array[largest]:
        largest = left
    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)

def heapSort(array: list) -> list:
    n = len(array)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]  # Swap
        heapify(array, i, 0)

    return array


unsorted_list = list(map(int, input("Enter numbers separated by spaces: ").split()))

sorted_list = heapSort(unsorted_list)
print(sorted_list)

# Input size: n
# Basic operation: comparison and swaps
# Time complexity: O(n*log(n))
