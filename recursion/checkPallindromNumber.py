
n = 12345

def pallindrom(old,check,new=0):

	if old == 0  and new ==check:
		return True
	if old ==0 and new	!= check:
		return False


	return pallindrom(old//10,check,(new *10 )+ (old%10))

res = pallindrom(n,n)
if res :
	print(n,"is pallindrom")
else:
	print(n,"is not a pallindrom")

