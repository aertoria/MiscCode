#!/usr/bin/python

class ListNode:
	def __init__(self,x):
		self.val = x
		self.next = None
		

node1=ListNode(1)
node2=ListNode(2)
node3=ListNode(3)

node1.next = node2
node2.next = node3


#print node1
#print node1.val
#print node1.val

'''
class Solution:
	# @param {ListNode} head
	# @return {ListNode}
	def reverseList(self, head):
		prev = None
		while head:
			curr = head
			head = head.next
			curr.next = prev
			prev = curr
		return prev#that is the end link of the list, thus the new head
'''




class Solution:
	# @param {ListNode} head
	# @return {ListNode}
	def reverseList(self, head):
		if head == None:
			return None
		elif head.next == None:
			return head
		else:
			pass
		current = head
		future = head.next
		head.next = None
		##next one
		while future.next:
			prev = current
			current = future
			future = future.next
			current.next = prev
		future.next = current
		return future

solution = Solution()
#newhead = solution.reverseList(node1)
#print newhead.val
#print newhead.next.val
#print newhead.next.next.val
returnnode = solution.reverseList(node1)
print returnnode.next.next.next




class Solution:
# @param {ListNode} head
# @return {ListNode}
	object=1
	def reverseList(self, head):
		if head == None:
			return None
		elif head.next == None:
			return head
		else:
			self.rec(head)
			return self.object

	def rec(self,node):
		#print node.next,node
		if node.next.next == None:
			node.next.next=node
			self.object = node.next
			return 'whatever'# this is node 3
		else:
			#print node.val
			self.rec(node.next)
			node.next.next=node
			node.next=None
		
		
