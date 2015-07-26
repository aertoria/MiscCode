#!/usr/bin/python

class Solution:
# @param {integer[]} nums
# @param {integer} k
# @return {boolean}
	def containsNearbyDuplicate(self, nums, k):	
		dict={}
		for location,value in enumerate(nums):
			dict.setdefault(value,[]).append(location)
		for key in dict:
			for i in range(len(dict[key])-1):
				if dict[key][i+1]-dict[key][i]<=k:
					return True
		return False
		
		
	def containsNearbyDuplicate2(self, nums, k):
		d = {}
		
		
		for position, value in enumerate(nums):
			d.setdefault(value,[]).append(position)
		
		print d
		for key in d:       
			if len(d[key]) > 1:             
				for i in range(0,len(d[key])-1):
					if abs(d[key][i] - d[key][i+1]) <= k:               
						return True
		return False
		
s=Solution()
nums=[1,0,1,1]
k=1
print s.containsNearbyDuplicate(nums,k)