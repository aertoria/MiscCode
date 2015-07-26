#!/usr/bin/python




class Solution:
	static_count=0
	# @param {string} s
	# @param {string} t
	# @return {integer}
	def numDistinct(self, s, t):
		self.re_search(s,t,0)
		print self.static_count
		return self.static_count
		
	def re_search(self,S,T,count):
		if len(T)==0:
			#print 'we finished one'
			self.static_count=self.static_count+1
			return 
		elif len(S)==0:
			#print 'we failed, they dont match'
			return
		elif T[:1]==S[:1]:#we found a match,now we have two choice, use it or not
			self.re_search(S[1:],T[1:],count+1)
			self.re_search(S[1:],T,count)
		else: #no match
			self.re_search(S[1:],T,count)
		


#S=ABCDBACD
#T=DC
S = "rabbbit"
T = "rabbit"

S ="aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
T ="bddabdcae"
solution = Solution()
solution.numDistinct(S,T)
