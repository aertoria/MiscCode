class c(object):
	t=990
	@staticmethod
	def f(i):
		c.t=i
		return i+1


	def g(self,i):
		self.t=i
		print self.t
		print c.t
		return i+2

	@classmethod # but classmethod let it access to class
	def h(self,i):#so cls means current class
		c.t=20
		self.t=10
		return i
	



c1=c()

#c1.h(10)
#print c1.g(1)
#c1.g(1)
#c.f(40)
#c1.g(1)

#c1.h(10)
c.h(15)

print c.t #  c's 
print c1.t # c1's cls


c2=c()
print c2.t


#print c1.t
#print c2.t
#print c2.f(2)
#print c2.g(2)