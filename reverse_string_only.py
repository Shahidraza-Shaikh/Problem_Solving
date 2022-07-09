from string import punctuation

punc = punctuation+" "

string = "A man, in the boat says : I see 1-2-3 in the sky" # only reverse string puctuation will be fixed

# # output  = y kse, ht ni3 21ee sIsy : a sta o-b-e ht nin amA

lis = list(string)

i = 0
j = len(lis)-1


while i <= j:

	if lis[i] in punc:
		i +=1
	if lis[j] in  punc:
		 j-=1

	if lis[i] not in punc and lis[j] not in punc :

		lis[i],lis[j] = lis[j],lis[i]

		i +=1
		j-=1


print(''.join(lis))





 








# num = '32666'

# dic = {1:'',2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z'],0:' '}

# freq = {}

# for i in num :

# 	freq[i] = freq.get(i,0) +1

# print(freq)








































