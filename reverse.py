#!/usr/bin/python
#Given s = "the sky is blue",
#return "blue is sky the".


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param {TreeNode} p
	# @param {TreeNode} q
	# @return {boolean}
	def isSameTree(self, p, q):
		if p==None and q==None:
			return True
		if p==None and q<>None:
			return False
		if p<>None and q==None:
			return False
		
		if (p.val == q.val) and (self.isSameTree(p.left,q.left)) and (self.isSameTree(p.right,q.right)):
			return True
		else:
			return False

		
		
		

s = Solution()

'''
00 - 0
01 - 1
11 - 3
10 - 2
'''