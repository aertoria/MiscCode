#!/usr/bin/python

class car(object):
	def __init__(self,brand):
		self.objectname='car'
		self.brand=brand
		
	def flashlight(self):
		print 'light flashed!'
		

class bmw(car):
	def __init__(self,color=None,*args, **kwargs):
		self.brand='bmw'
		self.color=color
		
		super(bmw,self).__init__(*args, **kwargs)
		
	def flashbeamlight(self):
		print 'this is strong beam light only on bmw'






my_bmw = bmw('red','bmw')
my_bmw.flashlight()
print my_bmw.objectname
print my_bmw.brand


def test(*args,**kwargs):
	print args
	print kwargs
	print "{AOS}-{KOS}".format(**kwargs)
	print "{},{}".format(*args)
	
test(1,2,3,[1,2,3],{1:23,213:230},AOS=12,KOS='LO')

