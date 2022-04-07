def max_ele(arr,i,j,max_idx):

    if i == j +1 :
        return max_idx
    elif arr[i] >  arr[max_idx]:
        max_idx = i

    i +=1
    return max_ele(arr,i,j,max_idx)

arr = [1,2,3,4,5,6,7]


def selection(arr,j=None,max_element_idx=0):
    if j is None:
        j = len(arr)-1

    if j == -1:
        return
    max_element_idx = max_ele(arr,0,j,0)

    print(arr,j,max_element_idx)
    arr[max_element_idx],arr[j] = arr[j],arr[max_element_idx]
    
    j -=1
    
    return selection(arr,j,max_element_idx)
selection(arr)
print(arr)
