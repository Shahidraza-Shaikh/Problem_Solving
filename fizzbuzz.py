# method 1 for fizzbuzz problem
dic ={}
# 
for num in range(1,101):
    if num %3 == 0 and num%5 == 0: #or we can write [num % 15 ==0] i.e 5*3 =15 
        dic[num]=("FizzBuzz")
        # count_both +=1
    elif num %3 ==0:
        dic[num]=("fizz")
        # count_3 +=1
    elif num %5 == 0 :
        dic[num]=("Buzz")
        # count_5 +=1
    else:
        dic[num] = num

print(dic)
# print("count both",count_both)
# print("Count 3",count_3)
# print("count 5",count_5)
