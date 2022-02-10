

def pallindrome(S):

	start = 0
	end = 0
	if len(S) ==0 :return ""
	for i in range(len(S)):
		len1 = devideFromMiddle(S,i,i)
		len2 = devideFromMiddle(S,i,i+1)
		print('len',len1,len2)
		break
		le = max(len1,len2)

		if le  > end - start :

			start = i - int((le-1)/2)

			end = i + int(le/2)
			print(start,end)

	return S[start:end+1]






def devideFromMiddle(S,left,right):

	if len(S) ==0 and left > right : return 0

	while left >=0 and right < len(S) and S[left] == S[right]:
		left -=1
		right +=1

	return right-left-1

print(pallindrome('aabbca'))