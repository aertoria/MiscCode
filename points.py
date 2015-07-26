#!/usr/bin/python

# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
	# @param {Point[]} points
	# @return {integer}
	
	result=[]
	def maxPoints(self, points):
		#print self.judge(points[0],points[2],points[3])
		#print self.judge(points[0],points[4],points[5])
		if len(points)==2:
			return 1
		if len(points)<=1:
			return 0
		
		
		index = 0
		while index < len(points)-2:
			index_2=index+1
			while index_2 <len(points)-1:
				#now the line has been set as points[index],points[index_2]
				length=0
				for p in points[index_2+1:]:
					if self.judge(points[index],points[index+1],points[index+2]):
						#print 'find one'
						length = length +1
				index_2=index_2+1
				self.result.append(length)
			index = index + 1
		print max(self.result)
		return max(self.result)
			
	
	def judge(self, point1,point2,point3):
		#if (point1.x-point2.x)/(point1.y-point2.y)=(point3.x-point2.x)/(point3.y-point2.y)
		if (point1.x-point2.x)*(point3.y-point2.y) == (point1.y-point2.y)*(point3.x-point2.x):
			return True
		else:
			return False
	
		
class Point:
	def __init__(self, a, b):
		self.x = a
		self.y = b





p1=Point(1,2)
p2=Point(3,5)
p3=Point(0,0)
p4=Point(9,5)
p5=Point(0,0)
p6=Point(2,4)

points = [[29,87],[145,227],[400,84],[800,179],[60,950],[560,122],[-6,5],[-87,-53],[-64,-118],[-204,-388],[720,160],[-232,-228],[-72,-135],[-102,-163],[-68,-88],[-116,-95],[-34,-13],[170,437],[40,103],[0,-38],[-10,-7],[-36,-114],[238,587],[-340,-140],[-7,2],[36,586],[60,950],[-42,-597],[-4,-6],[0,18],[36,586],[18,0],[-720,-182],[240,46],[5,-6],[261,367],[-203,-193],[240,46],[400,84],[72,114],[0,62],[-42,-597],[-170,-76],[-174,-158],[68,212],[-480,-125],[5,-6],[0,-38],[174,262],[34,137],[-232,-187],[-232,-228],[232,332],[-64,-118],[-240,-68],[272,662],[-40,-67],[203,158],[-203,-164],[272,662],[56,137],[4,-1],[-18,-233],[240,46],[-3,2],[640,141],[-480,-125],[-29,17],[-64,-118],[800,179],[-56,-101],[36,586],[-64,-118],[-87,-53],[-29,17],[320,65],[7,5],[40,103],[136,362],[-320,-87],[-5,5],[-340,-688],[-232,-228],[9,1],[-27,-95],[7,-5],[58,122],[48,120],[8,35],[-272,-538],[34,137],[-800,-201],[-68,-88],[29,87],[160,27],[72,171],[261,367],[-56,-101],[-9,-2],[0,52],[-6,-7],[170,437],[-261,-210],[-48,-84],[-63,-171],[-24,-33],[-68,-88],[-204,-388],[40,103],[34,137],[-204,-388],[-400,-106]]
newlist=[]


for item in points:
	#print item
	newlist.append(Point(item[0],item[1]))	
solution = Solution()
#solution.maxPoints([p1,p2,p3,p4,p5,p6])
#solution.maxPoints(newlist)

solution.maxPoints([])
