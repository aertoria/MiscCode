#!/usr/bin/python




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {TreeNode}
	def invertTree(self, root):
		self.DFS(root)
		if root <>None:
			self.switch(root)
		return root
	
	def DFS(self,node):
		if node == None:
			return
			
		self.DFS(node.left)
		if node.left<>None:
			self.switch(node.left)
			
		self.DFS(node.right)
		if node.right<>None:
			self.switch(node.right)
	
	def switch(self,node):
		exchange=node.left
		node.left=node.right
		node.right=exchange
		return

	
	
	
	
	
	
	
class TreeNode:
    def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

node4=TreeNode(4)
node7=TreeNode(7)
node2=TreeNode(2)
node9=TreeNode(9)
node6=TreeNode(6)
node3=TreeNode(3)
node1=TreeNode(1)
node4.left=node2
node4.right=node7
node2.left=node1
node2.right=node3
node7.left=node6
node7.right=node9



node=TreeNode(1)

s = Solution()
s.invertTree(node)
print node.val

