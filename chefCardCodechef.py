import math
N , X = map(int,input().split())
    
res = N - X 

if res <= 0:
    print(0)
    
if res >0 :
    count = 0
    print(math.ceil(res/4))
    # while res >=0 :
    #     # print(count)
    #     print(res)
        
    #     res -=4
    #     count +=1
        
# if res < 0 :
    
#     count +=1
    
#     print(count)