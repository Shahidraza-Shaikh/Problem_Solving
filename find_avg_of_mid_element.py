N1 = int(input())

N2 = int(input())

a = []
b = []

for i in range(N1):
	a.append(int(input()))

for j in range(N2):

	b.append(int(input()))

temp = sorted(set(a+b))

idx = len(temp)


mid = idx//2

if idx&1 ==0:
	print((temp[mid]+temp[mid-1])/2)
else:
	print(temp[mid])