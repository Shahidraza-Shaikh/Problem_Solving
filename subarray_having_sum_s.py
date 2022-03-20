

def subarray(arr,n,gsum):
	summ = arr[0]
	start  =1
	idx =1

	while idx <=n :

		while summ > gsum and start < idx -1 :
			# print(summ)
			summ -=arr[start]
			start +=1
		if summ == gsum :
			# print(summ)
			return start,idx -1

		if idx < n:
			summ += arr[idx]

		idx +=1


num = 8 #int(input())

lis =[15,2,4,8,9,5,10,23] #list(map(int,input().split(" ")))
summ = 23 # int(input())

print(subarray(lis,num,summ))