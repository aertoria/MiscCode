'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param {ListNode} head
	# @return {ListNode}
	static_list=[]
	def deleteDuplicates(self, head):
		self.rec_delete(head)
		

		if len(self.static_list)==0:
			return None
	
		listNodes = []
		for item in self.static_list:
			listNodes.append(ListNode(item))
		
		head = listNodes[0]
		i=0
		
		while(i<(len(listNodes)-1)):
			listNodes[i].next = listNodes[i+1]
			i=i+1
		listNodes[len(listNodes)-1].next = None
		
		return head
		
		
					
	def rec_delete(self,node):
		if node==None:
			return
		elif node.val in self.static_list:
			self.rec_delete(node.next)
		else:
			self.static_list.append(node.val)
			self.rec_delete(node.next)
		
		
class Solution:
	# @param {ListNode} head
	# @return {ListNode}
	def deleteDuplicates2(self, head):
		if not head:
			return None

		fast = slow = head
		fast = fast.next

		while fast:
			if slow.val != fast.val:
				slow = slow.next
				fast = fast.next
			else:
				fast = fast.next
				slow.next = fast

		return head
		
#1->1->2->3->3, return 1->2->3.
	
##head --> L1(1,next) --> L2(1,next) --> None
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
		
L1=ListNode(1)
L2=ListNode(1)
L3=ListNode(1)
L4=ListNode(4)
L5=ListNode(1)

L1.next = L2
L2.next = L3
L3.next = L4
L4.next = L5



s=Solution()
print s.deleteDuplicates2(L1).val
#print s.static_list
#print s.deleteDuplicates(L1).next.val
#print s.deleteDuplicates(L1).next.next