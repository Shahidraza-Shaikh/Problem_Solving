

def SortedSquaredArray(arr):
    i=len(arr)-1
    j=0
    k=len(arr)-1
    result = [0 for i in range(len(arr))]
    while i >=0:
        if abs(arr[j]) > arr[k]:
            # temp = arr[j]
            result[i] = arr[j] **2
            j +=1
        else:
            result[i] = arr[k] **2
            k -=1
        i -=1
    return result
arr=[-6,-4,1,2,3,5]
print(SortedSquaredArray(arr))