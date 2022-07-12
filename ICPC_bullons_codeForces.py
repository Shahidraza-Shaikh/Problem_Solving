# Questions :-  https://codeforces.com/contest/1703/problem/B

t = 1 #int(input())

for _ in range(t) :

	len_str = int(input())

	string = input()

	set_ =set()
	i = 0
	for s in string:
		if s not in set_:
			set_.add(s)

			i+=2
		else:

			i +=1
	print(i)

