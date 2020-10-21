def Binary_Search(A: list,low:int,hi:int, x: int):
    if hi >= low :
        mid = (hi + low) // 2
        if A[mid] == x:
            return mid
        elif A[mid] > x:
            return Binary_Search(A,low,mid -1 ,x)
        else:
            return Binary_Search(A,mid+1,hi,x)
    else:
        return -1


arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = Binary_Search(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index", str(result)) 
else: 
    print("Element is not present in array") 