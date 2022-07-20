
def Solution(string1,string2):
	
	ans = ''

	i=j = 0
	while i < len(string1) and j < len(string2):

		if string1[i] < string2[j] :

			ans	 +=string1[i]

			i +=1
		else:

			ans	 +=string2[j]

			j +=1

	while i < len(string1) :

		ans	 +=string1[i]
		i+=1

	while j < len(string2):

		ans	 += string2[j]
		j +=1

	return ans	 


print(Solution("DAVIDZ","ZROSE"))