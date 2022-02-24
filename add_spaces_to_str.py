

string = input()

num = int(input())

result = []

for i in range(0,len(string),num):

	result.append(string[i:i+num])

print(' '.join(result))


# shahid
# 2

# output :- 'sh ah id'