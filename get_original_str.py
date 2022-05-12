

strr = "AbcDef" #input()

m = 1 #int(input())

n = 2 #int(input())

res = ""
lenn = len(strr)
print(strr)

strr2  =strr
i = 0
while True:
	if strr != res:

		res =strr2[lenn-m:] + strr2[:lenn-m]
		i +=1

	if strr != res:
		res = res[lenn-n:] +res[:lenn-n]

		i +=1

	if strr == res:
		print(res)
		break

	strr2 = res

	

print(res,i)
