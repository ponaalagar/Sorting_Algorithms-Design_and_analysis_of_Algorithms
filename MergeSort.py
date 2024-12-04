#one of the divide and conquer technique

def mergeSort(A:list)->list:
    if len(A) <= 1:
        return A
    else:
        mid = len(A)//2
        A1 = A[:mid]
        A2 = A[mid:]
        A1 = mergeSort(A1)
        A2 = mergeSort(A2)
        A = merge(A1,A2,A)
        return A
    
def merge(A:list,B:list,C:list)->list:
    i=j=k=0
    p =len(A)
    q = len(B)

    while( i < p and j < q):
        if A[i] < B[j]:
            C[k] = A[i]
            i += 1
        else:
            C[k] = B[j]
            j += 1
        k += 1
    if i == p:
        C[k:] = B[j:]

    else:   
        C[k:] = A[i:]
    
    return C

input_string = input("Enter numbers separated by spaces: ")
array = list(map(int, input_string.split()))  # Convert input to a list of integers

# Sort the array
sorted_array = mergeSort(array)

# Print the sorted array
print("Sorted array:", sorted_array)   

#input size : n
#basic operation : comparison
#time complexity : O(n*log(n))

