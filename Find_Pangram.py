

import string

alpha = set(string.ascii_lowercase)

def isparam(input_str):
	return set(input_str.lower()) >=alpha



# Isangram function ke nadar likh niche wale linw ko

def pan(pangram):

	result = ""
	for line in pangram:

		res = isparam(line)

		if res:
			result +="1"
		else:
			result +="0"

	return result

print(pan(["abcdefghijklmnopqrstuvwxyz asad asd","abc def skdnf ghi jkl mno pqr stu vwxy z skdhf oifro"]))
