

def uniq_plants(li):

	count = 0
	if li[0] < li[1]:
		count +=1
	if li[-1] < li[-2]:
		count +=1
	for i in range(1,len(li)-1):

		if li[i-1] > li[i] and li[i] < li[i+1]:
			count +=1
		# elif li[i] < li[]
	print(count)


li = [2,8,96,32,2,5,2]
uniq_plants(li)

 
