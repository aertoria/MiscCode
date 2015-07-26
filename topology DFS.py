#!/usr/bin/python

class Solution:
	# @param {integer} numCourses
	# @param {integer[][]} prerequisites
	# @return {integer[]}
	def findOrder(self, numCourses, prerequisites):
		start = set()
		total = set()
		for pair in prerequisites:
			total.add(pair[0])
			total.add(pair[1])
			start.add(pair[0])
		
		if len(total-start)==0:
			return []
		start_course = (total-start).pop()
		
		self.prerequisites = prerequisites
		self.numCourses=numCourses
		

		self.stack = []
		self.result =[start_course]
		self.stack.append(start_course)
		self.DFS(start_course)
		#self.stack.pop()
		
		return self.result
		
	def DFS(self,current):
		if len(self.result)==self.numCourses:
			return
		
		for nextPair in self.prerequisites:
			if current == nextPair[1] and nextPair[0] not in self.stack:
				
				reqirement = True
				for futureprv in self.prerequisites:
					if futureprv[0]==nextPair[0]:
						reqirement=reqirement and (futureprv[1] in self.result)
				if not reqirement:
					continue 
					
				self.stack.append(nextPair[0])
				
				if nextPair[0] not in self.result:
					self.result.append(nextPair[0])
				self.DFS(nextPair[0])
				self.stack.pop()
		


numCourses = 4
prerequisites=[[1,0],[2,0],[3,1],[3,2]]
s=Solution()
print s.findOrder(1,[])

#print s.findOrder(2, [[0,1],[1,0]])