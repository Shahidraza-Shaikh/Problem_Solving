


def min_num(s):
	n = 9
	if s <10 :
		return s

	i = 9
	res = ""
	while i > 0 :

		temp = s - i

		if temp <  s   and temp >= 0:

			res +=str(i)

			s -=i

		i -=1

	return res[::-1]

print(min_num(20))








# def min_num(s):
# 	n = 9
# 	if s <10 :
# 		return s

# 	i = 9
# 	res = ""
# 	while i > 0 :

# 		temp = s - i

# 		if temp <  s   and temp >= 0:

# 			res +=str(i)

# 			s -=i

# 		i -=1

# 	return res[::-1]

# print(min_num(45))





