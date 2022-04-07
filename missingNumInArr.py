
def missingNumInArr(arr,n):

	sum_of_natutal_num = n*(n+1)//2

	total = 0

	for i in arr:
		total	 +=i

	return sum_of_natutal_num	- total	

arr= [1,2,3,4,5,6,7,8,10]
n = len(arr) +1

print(missingNumInArr(arr,n))