

def subarray(arr,n,gsum):
	summ = 0
	low =0
	high =1

	while low <=n :

		if summ < gsum :
			summ +=arr[high]
			high +=1
		if summ > gsum:
			print(summ)
			summ -=arr[low]
			low +=1
		if summ == gsum :
			print(summ)
			return low,high


num = int(input())

lis = list(map(int,input().split(" ")))
summ = int(input())

print(subarray(lis,num,summ))