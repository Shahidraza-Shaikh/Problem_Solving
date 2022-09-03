t = int(input())

for _ in range(t):

	num = int(input())

	value = input()
	result = []
	final_result = []
	x = 0
	count = 0
	while x < num :

		if value[x] =='R':

			count +=(num-1-x)
		else:

			count +=x 

		if value[x] == "R" and (x > (num-1-x)):

			result.append(2*x+1-num)
		elif value[x] == "L" and (x <(num-1-x)):

			result.append(num-1-2*x)
		x +=1

	result_temp = sorted(result,reverse=True)

	res = 0
	y = 0
	while y <len(result_temp):

		res += result_temp[y]

		final_result.append(count+res)

		y +=1

	start =len(result_temp)

	x = start

	while x < num:

		final_result.append(count+res)

		x +=1

	print(*final_result)




