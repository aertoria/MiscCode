#!/usr/bin/python

class Solution:
	# @param {integer} numCourses
	# @param {integer[][]} prerequisites
	# @return {integer[]}
	def findOrder(self, numCourses, prerequisites):
		#if prerequisites==[]:
		#	return range(numCourses)
		
		self.n=numCourses
		self.prerequisites=prerequisites
		
		self.loop=0
		self.visited={}
		
		for currentcourse in range(numCourses):
			if currentcourse in self.visited:
				continue
			self.stack=[currentcourse]
			self.DFS(currentcourse)
			#self.stack.pop()
		#print self.visited
		if self.loop==1:
			return []
		return sorted(self.visited,key = lambda x:self.visited[x])
	
	
	def DFS(self,course):
		if self.loop==1:
			return
		
		for next, current in self.prerequisites:
			if current == course and  next not in self.visited:
				if next in self.stack:
					self.loop=1
					#print 'has a loop here!!! stop immediately'
					return
				#I am going in
				self.stack.append(next)
				self.DFS(next)
				self.stack.pop()
		#when you return back:add current node to self.visited, with value self.n-1
		self.visited[course]=self.n	
		self.n=self.n-1	
		return
		






numCourses = 4
prerequisites=[[1,0],[2,0],[3,1],[3,2],[0,3]]
s=Solution()

print s.findOrder(3,[[1,0]])

#print s.findOrder(numCourses,prerequisites)