
initial_pos =0

testcase = int(input())

for _ in range(testcase):
	num = int(input())
	num = abs(num)
	if initial_pos >= 0:
		initial_pos	= initial_pos - num
		print(initial_pos)
	else:
		initial_pos	= initial_pos + num
		print(initial_pos)

