#!/usr/bin/python3
li=[]

# def MinPlus(start,end,x,y):

#     for i in range(end,len(x[end:])+1):

#         comput = 0

#         for j in range(i):
#             comput +=int(x[j])
#         var = comput + int(x[i:])

#         if var  == int(y):

#             return i
#     return -1
        


        

# st ='23=6'
# li = st.split("=")
# x=li[0]
# y=li[1]
# for i in range(len(x)-1):
#     result = MinPlus(i,i+1,x,y)

#     if result == -1:
#         print(-1)
#         continue
#     else:
#         print(result)
#         break


# num=6

A =[2,6]

# 6%2, 6%6

B =[12,24,36]

# 12%6  24%6  36%6 

def CommonNum():
    c = A + B
    
    for i in range(1,101):
        li=[]

        for ele in c :

            if ele < i :

                if i %ele ==0:
                    li.append(1)

            else:
                if ele % i ==0:
                    li.append(1)
        
        if sum(li) ==len(c):
            return i


print(CommonNum())

































