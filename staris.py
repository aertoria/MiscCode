#!/usr/bin/python

#You are climbing a stair case. It takes n steps to reach to the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


class Solution:
	# @param {integer} n
	# @return {integer}
	count=0
	def climbStairs(self, n):
		
		self.rec_climb(n)
		print self.count
		return self.count
		
	def rec_climb(self, n):
		if n==0:
			#print 'yeah success'
			self.count=self.count+1
		elif n<0:
			#print 'cannot climb this way'
			pass
		else:
			self.rec_climb(n-1)
			self.rec_climb(n-2)
		
		
		


solution=Solution()
solution.climbStairs(35)