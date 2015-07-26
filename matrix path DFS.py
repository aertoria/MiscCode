#!/usr/bin/python


class Solution:
	matrix=[]
	xlimit=0
	ylimit=0
	endpoint=[]
	stack=[]
	result=0
	
	def findpath(self,matrix,startpoint,endpoint):
		self.matrix = matrix
		self.xlimit=len(matrix)
		self.ylimit=len(matrix[0])
		self.endpoint=endpoint
		self.stack.append([startpoint[0],startpoint[1]])
		self.DFS(startpoint[0],startpoint[1])
		
		if self.result <> 0:
			return True
		return False
		
	
	def DFS(self,x,y):
		if x==self.endpoint[0] and y==self.endpoint[1]:
			print 'we reached it finally this is the path:', self.stack
			self.result+=1
			return
		if x+1<self.xlimit and self.matrix[x+1][y]==0 and [x+1,y] not in self.stack:
			self.stack.append([x+1,y])
			self.DFS(x+1,y)
			self.stack.pop()
		if x-1>=0 and self.matrix[x-1][y]==0 and [x-1,y] not in self.stack:
			self.stack.append([x-1,y])
			self.DFS(x-1,y)
			self.stack.pop()
		if y+1<self.ylimit and self.matrix[x][y+1]==0 and [x,y+1] not in self.stack: 
			self.stack.append([x,y+1])
			self.DFS(x,y+1)
			self.stack.pop()
		if y-1>=0 and self.matrix[x][y-1]==0 and [x,y-1] not in self.stack:
			self.stack.append([x,y-1])
			self.DFS(x,y-1)
			self.stack.pop()




matrix=[[0 for y in range(4)] for x in range(5)] 


matrix[3][0]=1
matrix[4][0]=1
matrix[1][1]=1

matrix[2][2]=1
matrix[4][2]=1

matrix[4][3]=1

startpoint=[0,0]
endpoint=[1,2]
s=Solution()
print s.findpath(matrix,startpoint,endpoint)

'''
matrix[2][0]=1
matrix[4][0]=1
matrix[1][2]=1
matrix[2][2]=1
matrix[3][2]=1
matrix[4][2]=1
matrix[1][3]=1
matrix[2][3]=1

startpoint=[4,1]
endpoint=[0,3]
s=Solution()
print s.findpath(matrix,startpoint,endpoint)
'''
