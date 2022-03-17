
string = "110100"

s1 = sorted(string)
s2 = sorted(string,reverse=True)

count1 = 0
count2 = 0


for s in range(len(string)):

	if string[s] != s1[s]:
		count1 +=1


for j in range(len(string)):

	if string[j] != s2[j] :

		count2 +=1
print(min(count1,count2)//2)