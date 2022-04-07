
def anagram(str1,str2):

	n1 = len(str1)
	n2 = len(str2)

	if n1 != n2:
		return 0

	str1 = sorted(str1)
	str2 = sorted(str2)

	for s in range(n1):

		if str1[s] != str2[s]:
			return 0

	return 1


str1 = "silent"
str2 = "listen"

if anagram(str1,str2):
	print(f"{str1} and {str2} is anagram of each other")
else:
	print(f"{str1} and {str2} is not anagram of each other")
