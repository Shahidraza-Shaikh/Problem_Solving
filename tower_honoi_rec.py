

num = int(input())

def TOH(n,from_start,from_end,from_mid):

	if n == 0:
		return 


	TOH(n-1,from_start,from_mid,from_end)

	print("move disk",n,"from rod",from_start,"to",from_end)

	TOH(n-1,from_mid,from_end,from_start)

TOH(num,"A","C","B")