
def Solution(num,q,x1,y1,x2,y2):

	answer = 0
	x = 0

	div = int(1e9) +7

	while x < num:

		answer += (q*(x1[x] * x1[x] + y1[x] * y1[x])) % div

		x +=1

	y = 0

	while y < q :

		answer += (num* (x2[y] * x2[y] + y2[y] * y2[y] )) % div

		y +=1


	addone = 0
	addtwo = 0
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

	justone = (justone * addone) % div

	justtwo = (justtwo * addtwo) % div

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













