#!/usr/bin/python


class Solution:
	# @param {integer} n
	# @return {integer}
	def numTrees(self, n):
		nlist=range(n+1)[1:]
		return self.rec(nlist)
		
	
	def rec(self,list):
		sum=0
		list=list[:]
		#print list
		if len(list)<=0:
			return 1
	
		for point in range(len(list)):
			#list[:point],list[point:]
			a=self.rec(list[:point])
			b=self.rec(list[point+1:])
			sum+=a*b
		#print 'return',sum
		return sum
			
	
		
		
		
s=Solution()
print s.numTrees(19)