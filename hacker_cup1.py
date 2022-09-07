test = int(input())

for  t in range(1,test+1):

	N,K = map(int,input().split())

	S = list(map(int,input().split()))

	if len(set(S)) > 2*K :
		print(f"Case #{t}:","NO")
		continue

	freq = {}
	flag = True
	for i in range(N):

		if S[i] in  freq:
			freq[S[i]] +=1
			if freq[S[i]] >2 :
				print(f"Case #{t}:","NO")
				flag = False
				break
		else:
			freq[S[i]] = 1

	if flag:
		print(f"Case #{t}:","YES")
