import re

s = input()

x = input()


# for i in range(len(s)) :

# 	if s [i] ==

# i = 0
# j = 0
# while i < len(s) :

# 	if x[j] == s[i] or 

if "*" in x :
	x = x.replace("*","[a-z]")

res = re.search(x,s)

print(res.start())