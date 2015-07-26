#!/usr/bin/python


#this is Q
#----
#
#----

class Stack:
	# initialize your data structure here.
	def __init__(self):
		self.Q = []
	
	# @param x, an integer
	# @return nothing
	def push(self, x):
		self.Q.append(x)
		return
		
	# @return nothing
	def pop(self):
		self.Q=self.Q[:-1]
		return

	# @return an integer
	def top(self):
		return self.Q[-1]
		
	# @return an boolean
	def empty(self):
		return len(self.Q)==0

s=Stack()
s.push(1)
s.pop
print s.Q[]
