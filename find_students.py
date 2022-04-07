


counter  = 0

input1 = 3#8
input2 = [48,51,40] #[44,45,56,39,2,6,17,75]
input3 = 5#1
input4 = [28,32,30,60,45]#[54]
for st in range(input3):

	for sub in range(input1):

		if input4[st] >= input2[sub]:
			counter +=1

print(counter) 


