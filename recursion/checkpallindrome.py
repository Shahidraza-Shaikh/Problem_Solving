

def isPallindrome(i,str1):

	if i >= len(str1)/2:
		return True

	if str1[i] != str1[len(str1)-i-1]:
		return False

	return isPallindrome(i+1,str1)

str1 = "MADAMA"

if isPallindrome(0,str1) == True:
	print(str1, "is  a Pallindrome")

else:
	print(str1,"not a Pallindrome")