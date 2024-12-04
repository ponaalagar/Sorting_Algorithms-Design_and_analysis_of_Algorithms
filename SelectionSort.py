#one of the brute force algorithm 

def selectionSort( array : list)->list:
    for i in range(len(array)-1):
        min_index = i
        for j in range(i+1,len(array)):
            if array[j]<array[min_index]:
                min_index = j
        array[i],array[min_index] = array[min_index],array[i]
    return array

#lets test the code 
unsorted_list = list(map(int,input().split()))
sorted_list = selectionSort(unsorted_list)
print(sorted_list)

#input size: n
#basic operation: comparison
#Time complexity : O(n^2)



