#!/usr/bin/python

class Solution:
	# @param {integer[]} nums
	# @param {integer} target
	# @return {integer[]}
	staic_result=[]
	def twoSum(self, nums, target):
		self.rec_find(nums,target,0)
		return self.staic_result
	
	
	def rec_find(self,nums,target,count):
		compare = target - nums[0]
		del nums[0]
		#print nums,compare
		if compare in nums:
			self.staic_result = [count,count+nums.index(compare)+1]
			return
		else:
			self.rec_find(nums,target,count+1)
			
			
			
s=Solution()

oSum([1,2],1 )