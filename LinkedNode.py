# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

class Solution:
	# @param {ListNode} l1
	# @param {ListNode} l2
	# @return {ListNode}
	def mergeTwoLists(self, a, b):
		if a and b:
			if a.val > b.val:
				a, b = b, a
			a.next = self.mergeTwoLists(a.next, b)
		return a or b
		
		
class Solution:
	# @param {ListNode} l1
	# @param {ListNode} l2
	# @return {ListNode}
	def mergeTwoLists(self, l1, l2):
		for item in l2:
			l1.append(l2)
		return l1
		
		
		
solution = Solution()

#l1=ListNode(10)

class ListNode:
	def __init__(self,x):
		self.val = x
		self.next = None

	def getData(self):
		return self.val

	def getNext(self):
		return self.next

	def setData(self,newdata):
		self.val = newdata

	def setNext(self,newnext):
		self.next = newnext



class LinkedList(object):
	def __init__(self, head=None):
		self.head = head
	
	def insert(self, data):
		new_node = ListNode(data)
		new_node.setNext(self.head)
		self.head = new_node


#solution.mergeTwoLists()

l=ListNode(2)
print l.next


l2=ListNode(1)
l.setNext(l2)



