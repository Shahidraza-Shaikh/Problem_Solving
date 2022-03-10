

def subarray(arr,n):
	ar=[]

	for i in range(n+1):
		# temp = []

		for j in range(i):
			if len(arr[j:i])>1 : 
				ar.append(arr[j:i])

		# ar.append(temp)s
		# temp.clear()
	print(ar)

ar = [1,2,3]

subarray(ar,len(ar))
