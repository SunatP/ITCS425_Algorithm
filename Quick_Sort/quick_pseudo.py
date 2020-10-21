def partition(A:list,low:int,hi:int):
    pivot = A[hi]
    small_elem = low - 1
    for j in range(low,hi) :
        if A[j]<pivot:
            small_elem += 1
            A[small_elem],A[j] = A[j],A[small_elem]
    A[small_elem+1] , A[hi] = A[hi], A[small_elem+1]
    return small_elem+1 

def Quicksort(A: list,low:int,hi:int): 
    if len(A) == 1:
        return A
    if low < hi :
        pivot = partition(A,low,hi)
        Quicksort(A,low,pivot-1)
        Quicksort(A,pivot+1,hi)


arr = [1,4,3,5,8,12,2]
n = len(arr)
Quicksort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])