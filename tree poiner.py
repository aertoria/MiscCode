#!/usr/bin/python
import threading,time

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution():
	# @param root, a tree link node
	# @return nothing
	def connect(self, root):
		if root == None:
			return
		if not isinstance(root,TreeLinkNode):
			return
		self.convert([root])
		
	def convert(self,nodelist):
		if len(nodelist)==0:
			return
		#change
		for i in range(len(nodelist)-1):
			nodelist[i].next=nodelist[i+1]
		nodelist[-1].next='NULL'
		#build next list
		nextlist=[]
		for node in nodelist:
			if node.left <> None:
				nextlist.append(node.left)
			if node.right <> None:
				nextlist.append(node.right)
		self.convert(nextlist)


class TreeLinkNode:
		def __init__(self, x):
			self.val = x
			self.left = None
			self.right = None
			self.next = None
			

class Runsolution(threading.Thread):
	def __init__(self):
		super(Runsolution,self).__init__()
	
	def run(self):
		t1 = TreeLinkNode(1)
		t2 = TreeLinkNode(2)
		t3 = TreeLinkNode(3)
		t4 = TreeLinkNode(4)
		t5 = TreeLinkNode(5)
		t6 = TreeLinkNode(6)
		t7 = TreeLinkNode(7)
		t1.left = t2
		t1.right = t3
		t2.left = t4
		t2.right = t5
		t3.left = t6
		t3.right = t7
			
		s=Solution()
		s.connect(t1)
		print t4.next.val,t5.next.next.val,t3.next
		print 'has been running for this thread'
		
		for i in range(5):
			print i
			time.sleep(0.4)
		




t=Runsolution()
t.start()
t=Runsolution()
t.start()
t=Runsolution()
t.start()
t=Runsolution()
t.start()
t=Runsolution()
t.start()



#5, 7, NULL
