num  = 5

def fact(num):
	if num==0 or num ==1:
		return 1
	return num * fact (num-1)


print(fact(num))