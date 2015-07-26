class node(object):
	def __init__(self,val):
		self.val=val
		self.right=None
		self.left=None
		




class Solution(object):
	def DFS_print(self,root):
		self.stack=[root]
		self.DFS(root)
		#self.stack.pop()
		
	def DFS(self,node):
		if node.left == None and node.right == None:
			#go back
			print map(lambda x:x.val,self.stack)
			return
		if node.left <> None: #if node.left<> None and node.left not in self.stack #in case it is a graph
			self.stack.append(node.left)
			self.DFS(node.left)
			self.stack.pop()
		if node.right<> None:
			self.stack.append(node.right)
			self.DFS(node.right)
			self.stack.pop()
		








##test cases
nodeA=node('A')
nodeB=node('B')
nodeC=node('C')
nodeD=node('D')
nodeE=node('E')
nodeF=node('F')
nodeA.left = nodeB
nodeA.right= nodeC
nodeB.left = nodeD
nodeC.left = nodeE
nodeC.right = nodeF

s=Solution()
s.DFS_print(nodeA)

	