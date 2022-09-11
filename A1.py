
def validate(y,z,c,d):

	a,b = 0,0

	while a < y and b < z:

		if c[a] == d[b]:

			a =a+1
			b =b+1

			if b == z:
				return True
		else:

			a = a - b+1
			b = 0

	return False

def Solution(num,k,x,y):

	if y == x :

		if k!=1 or k&1 ==0: return "YES"
		else: return "NO"

	if num == 2 :

		if   k %2 ==0and x == y :return "YES"
		elif k%2 !=0 and x==y : return "NO"
		elif  k%2 !=0 and x != y: return "YES"
		else: return "NO"

	x = x + x 

	result = validate(len(x),num,x,y)

	if k > 0 and result :return "YES"
	else: return "NO"

test = int(input())

for t in range(1,test+1):

	number,k = map(int,input().split())

	arrA = list(map(int,input().split()))

	arrB = list(map(int,input().split()))

	print(f"Case #{t}:",Solution(number,k,arrA,arrB))




