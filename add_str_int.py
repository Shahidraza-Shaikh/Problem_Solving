
num1  = int(input())

string = list(map(str,input().split(' ')))

num2  = int(input())

numbers = list(map(str,input().split(' ')))

result = ''

total = num1+num2
for i in range(num1):

	result = result+ " " + string[i]
	result = result+ " " + numbers[i]


print(result.strip())
