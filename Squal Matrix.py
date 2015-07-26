#!/usr/bin/python
'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.

'''

class Solution:
	# @param {character[][]} matrix
	# @return {integer}
	matrix=[]
	size=0
	
	def maximalSquare(self, matrix):
		if matrix==[]:
			return 0
		self.matrix=matrix
		result=[]
		for y in range(len(matrix[0])):
			for x in range(len(matrix)):
				self.size=0
				self.scan(x,y,x,y)
				result.append(self.size)
		return max(result)*max(result)
		

	def scan(self,start_x,start_y,x,y):
		for every_y in range(start_y,y+1):
			if self.matrix[x][every_y]=='0':
				return
		for every_x in range(start_x,x+1):
			if self.matrix[every_x][y]=='0':
				return
		self.size+=1
		if x+1<len(self.matrix) and y+1<len(self.matrix[0]):
			self.scan(start_x,start_y,x+1,y+1)
			






matrix=[[0 for y in range(4)] for x in range(5)]

matrix[0][0]=1
matrix[2][0]=1
matrix[0][1]=1
matrix[2][1]=1
matrix[3][1]=1
matrix[4][1]=1
matrix[0][2]=1
matrix[1][2]=1
matrix[2][2]=1
matrix[3][2]=1
matrix[4][2]=1
matrix[0][3]=1
matrix[3][3]=1
s=Solution()
#print s.maximalSquare(matrix)


print s.maximalSquare([['1']])


