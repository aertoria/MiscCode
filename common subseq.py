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

r a b b b i t
r a b b   i t



S=DABCDBACD

T=ADC

class Solution:
	def re_search(self,S,T,count):
		if len(T)==0 or len(S)==0:
			return
		elif T[:1]==S[:1]:#we found a match,now we have two choice, use it or not
			self.re_search(S[:1],T[:1],count+1)
			self.re_search(S,T[:1],count)
		else: #no match
			self.re_search(S[:1],T,count)

S = "rabbbit"
T = "rabbit"
solution = Solution()
solution.numDistinct(S,T)






class Solution:
	super_list_log=[]
	list_log=[]
	# @param {string} s
	# @param {string} t
	# @return {integer}
	def numDistinct(self, s, t):
		list_s=' '.join(s).split(' ')#r a b b b i t
		list_t=' '.join(t).split(' ')#r a b b   i t
		
		
		#print list_t[0]
		#ind=s.find(list_t[0])
		#self.list_log.append(ind)
		
		#print self.swip(s,list_t,0,0)
		self.super_list_log.append(self.list_log)
		

		
		print self.ramdonGenerator(list_s)
		
		'''
		if ind>-1:
			ind=s.find(list_t[1],ind)
			self.list_log.append(ind)
			if ind>-1:
				ind=s.find(list_t[2],ind)
				self.list_log.append(ind)
		'''
		
		self.logprint(s)
		return 1
		
	#@staticmethod
	#swip will launch a signle swip to do a match
	def swip(self,s,list_t,index_t,ind):
		ind_result = s.find(list_t[index_t],ind)
		if ind_result<-1:
			print 'Nothing found'
			return 'Nothing found'
		elif index_t+1==len(list_t):
			self.list_log.append(ind_result)
			print 'found this match'
			return 'found this match'
		else:
			self.list_log.append(ind_result)
			print 'recursive matching on %s at T.%i and at S.%i'%(list_t[index_t],index_t,ind_result)
			self.swip(s,list_t,index_t+1,ind_result+1)
			

	def ramdonGenerator(self,list_s):
		num=1
		while num<=len(list_s):
			print num
			
			
			num=num+1
	
	
	
	
	#This print out the log
	def logprint(self,s):
		print '\n\n\nSOURCE get mattched:'
		print self.list_log
		list=[]
		for index in self.list_log:
			list.append(s[index])
		print list


S = "rabbbit"
T = "rabbit"
solution = Solution()
solution.numDistinct(S,T)


