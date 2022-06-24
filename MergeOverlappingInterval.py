# Question  https://www.geeksforgeeks.org/merging-intervals/

def MergeOverlapInterval(interval):

	interval.sort()

	stack = []

	stack.append(interval[0])

	for i in interval[1:]:

		if  stack[-1][0] <= i[0] <= stack[-1][-1]:

			stack[-1][-1] = max(stack[-1][-1],i[-1])
		else:

			stack.append(i)

	return stack

interval = [[1,3],[2,4],[6,8],[9,10]]
# interval = [[6,8],[1,9],[2,4],[4,7]]

res = MergeOverlapInterval(interval)

print(res)