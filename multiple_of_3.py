

def multipleOfThree(num):

	if num<0:
		num = -num
	if num==0:
		return 1

	if num==1:
		return 0

	odd_count = even_count= 0

	while num :

		if num &1:
			odd_count +=1

		if num&2:
			even_count	+=1

		num = num>>2

	return multipleOfThree(abs(odd_count - even_count ))

num = 28
if multipleOfThree(num):
	print(num,"is multiple of 3")
else:
	print(num,'not multiple of 3')


