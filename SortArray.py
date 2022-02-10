#!/usr/bin/python3

# print ("Hello, Python!")
l=[1,15,18,20]
r=[5,10,15,20]
# new_arr = l+r
arr=[1,18,15,10,20,15,20,5]

# def SortArray(l,r,arr):
#     j=0
#     # k=len(arr) -len(l)
#     k=0
#     for i in range(len(arr)):
#         try :
        
#             if l[j] <= r[k]:
#                 arr[i] = l[j]
#                 j+=1
#                 # arr[i+1]=r[i]
                
                
#                 # print('arr',arr)
                
#             else:
#                 arr[i] = r[k]
#                 k+=1
#                 # arr[i+1] = l[i]
#         except:
#             # arr.pop()
#             arr.append(r[-1])
            

#     return arr
# print(SortArray(l,r,arr)) 

i=0

# for i in range(len(r)):
#     temp1 = min(l)
#     temp2 = min(r)
#     temp3=min(temp1,temp2)
#     if temp3 == temp1:
#         arr[i] = 

# l=[1,15,18,20]
# r=[5,10,15,20]
# # new_arr = l+r
# arr=[1,18,15,10,20,15,20,5]

x=0
while i < len(l):
    temp = min(l)
    temp1 = min(r)
    temp3 = min(temp,temp1)
    
    if temp3 == temp:
        arr[x] = temp3
        arr[x+1] = temp1
    else:
        arr[x] = temp1
        arr[x+1] = temp3
    l.remove(temp)
    r.remove(temp1)
    i +=1
    x+=2
print(arr)
