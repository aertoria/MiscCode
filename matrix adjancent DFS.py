#!/usr/bin/python
class Solution:
	matrix=[]
	xlimit=0
	ylimit=0
	stack=[]
	total_covered=[]
	current_covered=[]
	result=[]
	
	
	Q=[]

	def findarea(self,matrix):
		self.matrix = matrix
		self.xlimit=len(matrix) #8
		self.ylimit=len(matrix[0])#5
		
		for y in range(self.ylimit):
			for x in range(self.xlimit):
				if matrix[x][y]==1 and [x,y] not in self.total_covered:
					self.current_covered = [[x,y]]
					self.stack=[[x,y]]
					
					self.DFS(x,y)
					
					if len(self.current_covered) > 1:
						self.result.append(self.current_covered)					
						for pair in self.current_covered:
							 self.total_covered.append(pair)
		return self.result
			
		

	def DFS(self,x,y):
		#go right
		if x+1<self.xlimit and self.matrix[x+1][y]==1 and [x+1,y] not in self.stack:#can go: (check limit, value is 1, not in stack)
			self.stack.append([x+1,y])#push future node to stack
			self.current_covered.append([x+1,y])# push future node to current coverage list
			self.DFS(x+1,y)#move forward
			self.stack.pop()
			
		#go left
		if x>0 and self.matrix[x-1][y]==1 and [x-1,y] not in self.stack:#can go: (check limit, value is 1, not in stack)
			self.stack.append([x-1,y])#push future node to stack
			self.current_covered.append([x-1,y])# push future node to current coverage list
			self.DFS(x-1,y)#move forward
			self.stack.pop()
			
		#go down
		if y+1<self.ylimit and self.matrix[x][y+1]==1 and [x,y+1] not in self.stack:#can go: (check limit, value is 1, not in stack)
			self.stack.append([x,y+1])#push future node to stack
			self.current_covered.append([x,y+1])# push future node to current coverage list
			self.DFS(x,y+1)#move forward
			self.stack.pop()
			
		#go up
		if y>0 and self.matrix[x][y-1]==1 and [x,y-1] not in self.stack:#can go: (check limit, value is 1, not in stack)
			self.stack.append([x,y-1])#push future node to stack
			self.current_covered.append([x,y-1])# push future node to current coverage list
			self.DFS(x,y-1)#move forward
			self.stack.pop()
		return
		
		
		def BFS(x,y):
			pass
			
		
		
		
		
		
		
		



matrix=[[0 for y in range(5)] for x in range(8)] 
matrix[7][0]=1
matrix[7][1]=1
matrix[4][1]=1
matrix[3][2]=1
matrix[1][3]=1
matrix[2][3]=1
matrix[3][3]=1
matrix[4][3]=1
matrix[4][4]=1


s=Solution()
result=s.findarea(matrix)

for i in result:
	print i