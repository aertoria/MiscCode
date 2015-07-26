#!/usr/bin/python

'''
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

0 1 2 3 4 5 6
r a b b b i t
r a b b   i t
r a   b b i t
r a b   b i t


Return 3.
'''


class Solution:
	# @param {string} s
	# @param {string} t
	# @return {integer}
	result=0
	def numDistinct(self, s, t):
		list_s=' '.join(s).split(' ')#r a b b b i t
		list_t=' '.join(t).split(' ')#r a b b   i t
		self.rec_search(0,0,list_s,list_t)
		print self.result
		return self.result
		
	def rec_search(self,index_t,index_s,list_s,list_t):		
		while index_s < len(list_s):
			target=list_t[index_t]
			if list_s[index_s] == target:
				#print index_s,list_t[index_t]
				if index_t+1<len(list_t):
					self.rec_search(index_t+1,index_s+1,list_s,list_t)
				else:
					#print 'found finally a match'
					self.result=self.result+1
			index_s = index_s+1	
		return 1
		
		
S = "BABCDABCA"
T = "ABC"

S = "rabbbit"
T = "rabbit"

S="aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
T="bddabdcae"
solution = Solution()
solution.numDistinct(S,T)


