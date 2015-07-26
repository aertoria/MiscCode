#!/usr/bin/python

class BSTnode:
	def __init__(self):
		self.val=None
		self.left=None
		self.right=None
	
class BST:
	def __init__(self):
		self.root=BSTnode()
	
	def __str__(self):
		#this function print out a tree
		print 'root:',self.root.val
		self.rec_print(self.root,'')
		return ''
		
	def rec_print(self,node,indent):
		#will print the current node
		#print indent+'node:',node.val
		if node.left != None:
			indent+='\t'
			print indent+'left:',node.left.val
			self.rec_print(node.left,indent)
			indent=indent[1:]
		if node.right !=None:
			indent+='\t'
			print indent+'right:',node.right.val
			self.rec_print(node.right,indent)
			indent=indent[1:]
		return
		
		
	def insert(self,newnode):
		self.newnode=newnode
		self.rec_insert(self.root)
		
	def rec_insert(self,node):
		if self.newnode.val < node.val:
			if node.left==None:
				node.left = self.newnode
				return
			self.rec_insert(node.left)
		else:
			if node.right==None:
				node.right = self.newnode
				return
			self.rec_insert(node.right)
		
		
'''
tree=BST()
tree.root.val=7

node5=BSTnode()
node5.val=5
node2=BSTnode()
node2.val=2
node1=BSTnode()
node1.val=1
tree.insert(node2)
tree.insert(node5)
tree.insert(node1)
#after insertion

node3=BSTnode()
node3.val=3
node6=BSTnode()
node6.val=6
node12=BSTnode()
node12.val=12

tree.insert(node12)
tree.insert(node3)
tree.insert(node6)
print tree
'''


class Solution:
	# @param {integer} n
	# @return {integer}
	def numTrees(self, n):
		target=range(1,n+1)
		self.result=[]
		#print target
		
			
			
		#print self.tree
		self.list=[]
		self.build(target)
		self.list
		for sequence in self.list:
			print sequence
		
	
	stack=[]
	def build(self,pool):
		if len(pool)==0:
			self.list.append(self.stack[:])
		
		for next in pool:
			new_pool=pool[:]
			new_pool.remove(next)
			self.stack.append(next)
			self.build(new_pool)
			self.stack.pop()
		




s=Solution()
s.numTrees(3)
