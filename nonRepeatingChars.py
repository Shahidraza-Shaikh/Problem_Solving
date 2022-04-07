
def nonRepeatingChar(string):
	temp ={}
	val=''
	for i in string:

		temp[i] = temp.get(i,0) +1

	for s in string:
		if temp[s] == 1:
			val = s
			break
	return val


print(nonRepeatingChar('xzvczbtxyzvy'))

# xzvczbtxyzvy
