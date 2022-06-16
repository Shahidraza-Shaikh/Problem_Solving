
t = int(input())



# N,M = 7,3

def function(N,M):

	flag = False

	if N&1 and M >N//2 +1:
		flag = True
	if (N==M and N > 1)or M>N or flag:
		return -1
	if N==M:
		return 'a'

	strr = ''
	res = N//2
	ascci = 97
	i = 0
	for i in range(res):
		# print(i)

		if i < M :
			# print(i,M)

			strr +=chr(ascci)

			ascci +=1

	temp_res = len(strr)
	# print(strr,N//2)
	while temp_res < N//2:
		# print(temp_res)
		strr += chr(ascci-1)

		temp_res +=1
	# print(ascci,chr(ascci))
	if N &1 :

		if  M >= N//2 +1:
			strr +=chr(ascci)
			strr += strr[::-1][1:]
		else:
			strr += chr(ascci-1)
			strr += strr[::-1][1:]

	else:
		strr += strr[::-1]


	print(strr)

print(function(N,M))

for _ in range(t):
	N,M = map(int,input().split(' '))

	function(N,M)


