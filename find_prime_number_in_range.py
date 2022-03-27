
n = 12

bool_val = [True]*(n+1)
print(bool_val)
bool_val[0] = False
bool_val[1] = False
print(bool_val)
def find_prime(bool_val,n):

	# for i in range(2,n+1)
	i = 2
	while i*i <=n :
		# print(i,bool_val[i])

		j = 2*i

		while j <= n:

			bool_val[j] = False

			j +=i

		# for j in range(2*i,n+1,j+=i):
		# 	bool_val[j] = False



		i+=1


	return bool_val

is_prime = find_prime(bool_val,n)

for i in range(n+1):
	print(i,is_prime[i])