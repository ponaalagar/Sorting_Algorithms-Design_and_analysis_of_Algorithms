# It is a simple sorting technique where elements are inserted into their correct position . it is one of the decrease and conquer technique

def insertionSort(array: list) -> list:
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        # Move elements of array[0..i-1] that are greater than key to one position ahead
        # of their current position
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

unsorted_list = list(map(int, input("Enter numbers separated by spaces: ").split()))

sorted_list = insertionSort(unsorted_list)
print(sorted_list)

# Input size: n
# Basic operation: comparison and shifting
# Time complexity: O(n^2)
