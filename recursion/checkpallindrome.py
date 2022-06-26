

def isPallindrome(i,str1,n):

	if i >= n/2:
		return True

	if str1[i] != str1[n-i-1]:
		print(str1[i],str1[n-i-1])
		return False

	return isPallindrome(i+1,str1,n)

str1 = "MADAM"

if isPallindrome(0,str1,len(str1)) == True:
	print(str1, "is  a Pallindrome")

else:
	print(str1,"not a Pallindrome")