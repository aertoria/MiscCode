#!/usr/bin/python


class Solution:	
	# @param {integer} m
	# @param {integer} n
	# @return {integer}
	def uniquePaths(self, m, n):
		matrix=[[0 for y in range(n+1)] for x in range(m+1)] 
		matrix[0][1]=1
		y=1
		while y<=n:
			x=1
			while x<=m:
				matrix[x][y]=matrix[x-1][y]+matrix[x][y-1]
				#print matrix[x-1][y],'+',matrix[x][y-1],'=',matrix[x][y]
				x+=1
			y+=1
		return matrix[m][n]
		
		
		
s=Solution()
print s.uniquePaths(23,12)







'''
dumb way, recursive DFS all the way.
class Solution:	
	matrix=[]
	xlimit=0
	ylimit=0
	result=0
	# @param {integer} m
	# @param {integer} n
	# @return {integer}
	def uniquePaths(self, m, n):
		self.xlimit=m
		self.ylimit=n
		self.matrix=[[0 for y in range(n)] for x in range(m)] 
		
		self.find_path(0,0)
		return self.result 
		
		
		
	def find_path(self,x,y):
		if x==self.xlimit-1 and y==self.ylimit-1:
			self.result+=1
			return 
		if x+1<self.xlimit:#can move left
			self.find_path(x+1,y)
		if y+1<self.ylimit:#can move down
			self.find_path(x,y+1)
		pass
'''
