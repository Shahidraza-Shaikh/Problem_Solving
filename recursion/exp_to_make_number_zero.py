

def expresion(num,sg,exp):
	print(num,exp)

	if num ==0:

		if eval(exp[:-1][::-1]) == 0:

			print(exp)
		return

	# exp += f"{sg}+"

	expresion(num//10,num%10,exp+(str(sg)+"+"))

	# exp += f"{sg}-"

	expresion(num//10,num%10,exp+(str(sg)+"-"))

num = 35132
sg = num%10

expresion(num,sg,"")