


def power(M,N) :

	ans = 1

	while N > 0 :

		last_bit = (N&1)

		if last_bit :

			ans = ans* M

		M *= M

		N >>= 1
	return ans

print(power(2,4))