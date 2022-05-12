testacase  = int(input())

for _ in range(testacase):

	num = int(input())

	string = input()

	di = dict.fromkeys("01",0)

	for i in string:
		if i in di:

			di[i] += 1

	if  di['1'] == di['0']:
		print(di['0']+di['1'])
	elif di['1'] > di['0']:
		print(di['0']*2+1)
	elif di['0']>di['1']:
		print(di['1']*2+1)
	else:
		print(1)