def sortArr(arr):
	result =''
	arr = sorted(arr)
	for i in arr[0]:
		if i != arr[0][-1]: 
			result += (i +'***')
		else:
			result += i

	return  result

arr = ['bitcoin','take','over','the','world','maybe','who','knows','perhaps']
print(sortArr(arr))

def insertion(arr):

	for i in range(1,len(arr)):
		key = arr[i]
		j = i - 1

		while j >= 0 and arr[j] >key :
			arr[j+1] = arr[j]
			j -=1

		arr[j+1] = key
	return arr

def sortArrAndPP(arr) :
	dic = {ord(i[0]) :i for i in arr}
	arr = sorted(dic)
	arr = insertion(arr)
	string = dic[arr[0]]
	return string[0]+string[1: len(string)-1].replace('','***')+ string[-1]
print(sortArrAndPP(arr))