



def mergeList(list1,n1,list2,n2,res):

	if n1 >= len(list1) :
		res += list2
		return
	if n2 >= len(list2):
		res +=list1

		return

	if list1[n1] < list2[n2]:
		res.append(list1[n1])

		mergeList(list1,n1+1,list2,n2,res)
	else:
		res.append(list2[n2])
		mergeList(list1,n1,list2,n2+1,res)

	return res

list1 = [1,3,3,5,6,7]

list2 = [2,4,4]

res = []

mergeList(list1,0,list2,0,res)

print(res)
