def insertionSort(arr): 
  
    for j in range(1, len(arr)): 
  
        key = arr[j] 
        i = j-1
        while i >=0 and key < arr[i] : 
                arr[i+1] = arr[i] 
                i -= 1
        arr[i+1] = key 
  
   
arr = [12, 11, 13, 5, 6] 
insertionSort(arr) 
print ("Sorted array is:") 
for i in range(len(arr)): 
    print (arr[i]) 
	

	------------------------------------------------------------------
	
	
	def SelectionSort(A):
    for i in range(0, len(A) - 1):
        smallest = i
        for j in range(i + 1, len(A)):
            if A[j] < A[smallest]:
                smallest = j
        A[i], A[smallest] = A[smallest], A[i]
 
 
A = input('Enter the list of numbers: ').split()
A = [int(x) for x in A]
SelectionSort(A)
print('Sorted list: ', end='')
print(A)

====================================================================================


def bubblesort(A):
    lengthOfArray = len(A) - 1
    for i in range(lengthOfArray):
        for j in range(lengthOfArray - i):
            if A[j] < A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]

    return A


 
A = input('Enter the list of numbers: ').split()
A = [int(x) for x in A]
bubblesort(A)
print('Sorted list: ', end='')
print(A)


======================================================================================



def counting_sort(A, largest):
    c = [0]*(largest + 1)
    for i in range(len(A)):
        c[A[i]] = c[A[i]] + 1

    c[0] = c[0] - 1 
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]
 
    result = [None]*len(A)
    for x in reversed(A):
        result[c[x]] = x
        c[x] = c[x] - 1
 
    return result
 
 
A = input('Enter the list of (nonnegative) numbers: ').split()
A = [int(x) for x in A]
k = max(A)
sorted_list = counting_sort(A, k)
print('Sorted list: ', end='')
print(sorted_list)

================================================================================
def mergeSort(A):
    if len(A) > 1:
        mid=len(A)//2;left=A[:mid];right = A[mid:];mergeSort(left);mergeSort(right);i=j=k=0;
        
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                A[k]=left[i];i+=1
            else:
                A[k]=right[j];j+=1
            k+=1
        # For all the remaining values
        while i<len(left):
            A[k]=left[i];i+=1;k+=1
        while j<len(right):
            A[k]=right[j];j+=1;k+=1
A = input('Enter the list of numbers: ').split()
A = [int(x) for x in A]
mergeSort(A)
print("The Merge Sort Result: ",*A)
