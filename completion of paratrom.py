#!/usr/bin/python

'''
Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".

'''

class Solution:
	# @param {string} s
	# @return {string}
	def shortestPalindrome(self, s):
		self.stringlist=list(s)
		self.result=''
		self.compare(self.stringlist)
		return self.result
	
	def compare(self,string):
		if len(string)==0:
			return
		
		index = (len(string)+1)/2
		indicator = (len(string)+1)%2
		
		#print index,indicator
		current=string[:]
		if indicator == 1:
			#current[:index],current[index:]
			part=current[:index]
			part.reverse()
		 	if part==current[index:]:
				remove = 2*len(current[:index])
				completion = self.stringlist[remove:]
				completion.reverse()
				self.result=''.join(completion+self.stringlist)
				return
		else:
			#print current[:index-1],current[index:]
			part=current[:index-1]
			part.reverse()
			if part==current[index:]:
				remove = 2*len(current[:index-1])+1
				completion = self.stringlist[remove:]
				completion.reverse()
				self.result=''.join(completion+self.stringlist)
				return
		#This run didn't found any
		self.compare(current[:-1])

			
s=Solution()
string='abababababaaaaabbbbbababababab'

print s.shortestPalindrome(string)
#print s.shortestPalindrome(st)#remvoed an a dcbabcd dcbabcd
		