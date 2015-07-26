#!/usr/bin/python
class Solution:
	# @param {string} s
	# @return {boolean}
	def isValid(self, s):
		slist=' '.join(s).split(' ')
		print slist
		stack=[]
		
		for item in slist:
			if item in ('[','{','('):
				stack.append(item)
			else:
				if len(stack)==0:
					return False 
				elif stack[-1:][0]==self.rev(item):
					stack = stack[:-1]
				else:
					return False
		if len(stack)==0:
			return True
		else:
			return False
	
	def rev(self,item):
		if item == ']':
			return '['
		elif item == '}':
			return '{'
		else:
			return '('
			
			

s=Solution()
print s.isValid(']')