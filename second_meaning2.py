test = int(input())

class Compute2:

	def __init__(self,data1=None,data2=None):
		self.data1 = data1
		self.data = data2

	def verify(self,val1,val2):

		for x in range(len(val1)):

			if val1[x] != val2[x] :
				return False
		return True



class Main2:

	def __init__(self,var1=None,var2=None):

		self.var1 = var1
		self.var2 = var2

	def function(self,number,temp):
		
		number -=1

		for varx in range(1024):

			just = ""

			for  vary in range(10) :

				if (varx>>vary)&1 :  
					just = just + "."

				else:  
					just +="-"


			comp = Compute2()
			if not comp.verify(temp,just) and not comp.verify(just,temp):

				number -=1

				print(just)

				if number==0 : return






for x in range(1,test+1):

	num = int(input())

	strr = input()


	print("Case #{}:".format(x))
	obj = Main2()
	obj.function(num,strr[:10])