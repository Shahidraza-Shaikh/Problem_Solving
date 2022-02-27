
ch = input()
num = int(input())

chars = [ chr(i) for i in range(97,123)]


char_idx = chars.index(ch.lower())

char_idx = (char_idx + num)%26

if ch.isupper():
	print(chars[char_idx].upper())
else:
	print(chars[char_idx])



 