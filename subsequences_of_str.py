
string ='abc' # input()

def subseq(string,output):

	if len(string) == 0:

		output[0] =""

		return 1

	outputSize = subseq(string[1:],output)

	for i in range(outputSize):
		
		output[i+outputSize] = string[0] + output[i]

	return outputSize *2

output = ["1" for i in range(2**len(string))]

l = subseq(string,output)

print(output)


