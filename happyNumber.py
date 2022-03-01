

num = int(input())

temp = num
while  num :
	l = []

	while num >0 :
		l.append(num%10)
		num //=10
	val = sum(list(map(lambda x : x**2,l)))
	num = val
	if len(str(num)) == 1:
		break

if num ==1 :
	print(temp,"is a happy number")
else:
	print(temp,"is not a happy number")


# input : 7

# output : 1 that 7 is a happy number

# explanation : 

# 7^2 = 49
# 4^2 + 9^2 = 97
# 9^2 + 7^2 = 130
# 1^2 + 3^2 + 0^2 = 10
# 1^2 + 0^2 = 1 so happy number otherwise not a happy number
