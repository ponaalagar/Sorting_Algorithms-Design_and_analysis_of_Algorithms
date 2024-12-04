#it is one of the divide and conquer technique to sort elements

def quickSort( array : list)->list:
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quickSort(left) + middle + quickSort(right)


unsorted_list = list(map(int,input().split()))

sorted_list = quickSort(unsorted_list)
print(sorted_list)

#input size : n
#basic operation : comparison
#time complexity : O(n*log(n))

