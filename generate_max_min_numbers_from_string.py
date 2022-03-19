

# def extract_max(ss):
# 	num,res=0,0

# 	for i in range(len(ss)):

# 		if ss[i] >= "0" and ss[i] <= "9":
# 			num = num *10 +int(int(ss[i])-0)

# 		else:
# 			res = max(res,num)
# 			num = 0

# 	return max(res,num)

# # ss = "100klh564abc365bg"
# ss = "A96T831NO0"

# print(extract_max(ss))

def smallest(ss):
	num = ""

	for i in ss :
		if i.isdigit():
			num +=i

	num = num.replace('0','')
	lst = list(num)
	lst.sort()

	for i,n in enumerate(lst):

		if n != '0':
			tmp = lst.pop(i)
			break
	return str(tmp) + ''.join(lst)

def max_num(ss):

	num = ""

	for i in ss :
		if i.isdigit():
			num +=i

	count = [ 0 for x in range(10)]

	string = str(num)

	for i in range(len(string)):
		count[int(string[i])]=count[int(string[i])]+1
		result = 0
		multiplier = 1

	for i in range(10):
		while count[i] >0:

			result = result + (i * multiplier)
			count[i] = count[i] -1
			multiplier = multiplier *10

	return result

num = input()

print(max_num(num))

print(smallest(num))