

def rec(summ,d):
	if int(summ)  <10 and int(summ)==d:
		return True

	if int(summ)  <10  and int(summ)!=d:

		return  False
			
	# else:
	# 	return "NO"
	else:
		sum1 = sum([int(summ[i]) for i in range(0,len(summ),2)])

		sum2 = sum([int(summ[i]) for i in range(1,len(summ),2)])
		
		return rec(str(sum1),d) or rec(str(sum2),d)

val = '1457823'
result = rec(val,7)
if result :
	print("YES")
else:
	print("NO")