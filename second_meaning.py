t = int(input())

class Compute:

	def __init__(self,data1=None,data2=None):
		self.data1 = data1
		self.data = data2

	def verify(self,val1,val2):

		for x in range(len(val1)):

			if val1[x] != val2[x] :
				return False
		return True



class Main:

	def __init__(self,var1=None,var2=None):

		self.var1 = var1
		self.var2 = var2

	def function(self,number,temp):
		
		number -=1
		varx = 0

		while varx <= 1023:

			vary = 0

			just = ""

			while vary <= 199 :

				if (varx>>vary)&1 : 
					just = just + "."

				else: 
					just +="-"

				vary +=1

			comp = Compute()
			if not comp.verify(temp,just) and not comp.verify(just,temp):

				number -=1

				print(just)

				if number==0 : return

			varx +=1





for i in range(1,t+1):

	number = int(input())

	string = input()


	print("Case #{}:".format(i))
	obj = Main()
	obj.function(number,string)