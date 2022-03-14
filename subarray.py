
# n = int(input())
from itertools import combinations
n = 3

# rank = int(input())
rank = 5

# strings = list(map(str,input().split(',')))

strings = ['abc','dab','bc']
# strings.sort()
sub_array = []

for i in range(n+1):

	for element in combinations(strings,i):
		# sub_array.append((len(strings[j:i]),strings[j:i]))
		sub_array.append(element)

print(sub_array)
print(','.join(sub_array[rank-1]))