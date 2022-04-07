
str1 = input()
str2 = input()
str3 = input()

def interleaving(st1,str2,str3):
	flag = True
	for s in str1:
		if s not in str3:
			flag = False
			return "str1 and str2 is not interleaving with str3"
	for s in str2 :
		if s not in str3:
			flag = False
			return "str1 and str2 is not interleaving with str3"
	if flag:
		return "st1 and st2 is  interleaving with str3"

print(interleaving(str1,str2,str3))


