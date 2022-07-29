

def product(N):


	total=1

	new_max_arr = 0
	for i in range(1,N):

		total *=i

		if total % N ==1:

			print(i,total)


			new_max_arr = i

	print(new_max_arr)

product(9)







