
# arr=[1,2,3,4,5,0,0,0,6,7,8,9,10]
# arr=[2,3,4,6,3,2,1,3,7,8,9]
arr = [2,3,4,6,3,2,1,3,2,3,1,7,8,9]
def longest(arr,s):
    left  =0
    right =0
    start =0
    end   =0
    total = arr[0]
    if sum(arr) < s:
        return "sum of array is less than s"
    else:

        while right < len(arr)-1:

            if total > s :
                total -= arr[left]
                left +=1
            
            else:
                right +=1
                total += arr[right]
            
            if total ==s:
                if (right -left) > (end-start):
                    start = left
                    end = right
    
    return arr[start:end+1]

print(f"longest array having sum 15 :\t",longest(arr,s=15))
    




        






















# # arr=[1,2,3,4,5,0,0,0,6,7,8,9,10]
# def LongestArray(arr,s):
#     left=0
#     right=0
#     start=0
#     end=0
#     total=arr[0]
#     while right <len(arr)-1:

#         if total >s:
#             total -=arr[left]
#             left +=1
#         else:
#             right +=1
#             total +=arr[right]
            
            
#         if total == s:
#             print(left,right)
#             if (right-left) > (end-start):
#                 start =left
#                 end = right

#     return arr[start:end+1]
        


# print(LongestArray(arr,s=55))