# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {integer}
	
	def countNodes(self, root):
		return self.DFS(root)
		
		
	def DFS(self,node):
		if node == None:
			return 0
		return self.DFS(node.left) + self.DFS(node.right) + 1
		
		
		
class TreeNode:		
	def __init__(self, x):
	    self.val = x
	    self.left = None
	    self.right = None
	


t1=TreeNode(1)
t2=TreeNode(2)
t3=TreeNode(3)
t4=TreeNode(4)
t5=TreeNode(5)
t1.left=t2
t1.right=t3
t2.left=t4
t2.right=t5
print ('I am Python')
s=Solution()
print s.countNodes(t1)