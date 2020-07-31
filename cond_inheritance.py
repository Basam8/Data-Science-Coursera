class p:
	def f1(self):
		print("p")
	def add(self):
		return "addded"
class c(p):
	def f2(self):
		print("c")

ob=c()
ob.f1()
ob.add()
ob.f2()