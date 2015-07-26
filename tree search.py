#!/usr/bin/python


class Solution:
	# @param {TreeNode} root
	# @return {integer[]}

	static_list=[]
	def rightSideView(self, root):
		self.rec_search(root,[])
		#print self.static_list
	
		max_list = self.static_list
		max_list=sorted(max_list,key=lambda x:len(x),reverse=True)
		max=len(max_list[0])
				
		result_path=[]
		i=0
		while i < max:
			for path in self.static_list:
				if len(path)>i:
					result_path.append(path[i])
					break
			i+=1
		return result_path

	  
	def rec_search(self,node,path):
		local = path[:]
		if node == None:
		   self.static_list.append(local)
		   return
		local.append(node.val)
		self.rec_search(node.right,local)
		self.rec_search(node.left,local)
		
	
	
	
		
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


n1=TreeNode(1)
n3=TreeNode(3)
n1.right=n3

	

s=Solution()
print s.rightSideView(n1)
