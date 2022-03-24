
testcase = int(input())

for _ in range(testcase):

	num__of_gp,chef_roll = map(int,input().split())
	num__of_gp *=2

	i = 1
	while i!= num__of_gp :

		if i == chef_roll :
			print(num__of_gp)
			break
		i +=1

		num__of_gp -=1
