#step 1 base case if idex(idx==len(arr) add sum to list )
#Step 2 take that element and add arr[idx] to sum var
#step 3 do not take that element and just pass the sum var only as we dont take the element.


def subSetSum(idx,arr,N,summ,ans):

	if idx == N:
		ans.append(summ)

		return

	subSetSum(idx+1,arr,N,arr[idx]+summ,ans)

	subSetSum(idx+1,arr,N,summ,ans)

	return ans



arr = [3,1,2]

N = len(arr)-1
summ = 0
print(subSetSum(0,arr,N,summ,[]))