def GetTheExponent(x, y, p):
 
    res = 1
 
    while (y > 0):
 
        if ((y & 1) != 0):
            res = res * x
 
        y = y >> 1 
        x = x * x 
 
    return res % p

def FindgcddofTwo(x, y):
 
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):
            res = i
             
    return res


def Solution(num,q,x1,y1,x2,y2):
	div = int(1e9) +7

	answer = 0
	x = 0


	while x < num:

		answer += (q*(x1[x] * x1[x] + y1[x] * y1[x])) % div

		x +=1

	y = 0

	while y < q :

		answer += (num* (x2[y] * x2[y] + y2[y] * y2[y] )) % div

		y +=1


	addone =addtwo = 0
	j = 0

	while j < q :

		addone = (addone  + x2[j]) % div

		addtwo = (addtwo + y2[j] ) % div

		j +=1

	justone =justtwo= 0

	i = 0
	while i < num:
		
		justone = (justone + 2 *x1[i]) % div

		justtwo = (justtwo + 2 * y1[i]) % div

		i +=1

	justtwo = (justtwo * addtwo) % div
	
	justone = (justone * addone) % div


	res = (justone + justtwo) % div

	answer -=res

	return answer % div


test = int(input())

for t in range(1,test+1):

	x1,x2,y1,y2  = [],[],[],[]

	number = int(input())
	j = 0
	
	while j < number :

		x,y = map(int,input().split())

		x1.append(x)
		y1.append(y)

		j +=1

	q = int(input())

	j = 0

	while j < q :

		x,y = map(int,input().split())

		x2.append(x)
		y2.append(y)

		j +=1

	print(f"Case #{t}:",Solution(number,q,x1,y1,x2,y2))













