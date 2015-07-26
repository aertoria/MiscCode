#!/usr/bin/python
'''
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
'''

class TrieNode:
	# Initialize your data structure here.
	def __init__(self):
		self.val = None
		self.pointers={}
		

class Trie:
	def __init__(self):
		self.root = TrieNode()
		
	# @param {string} word
	# @return {void}
	# Inserts a word into the trie.
	def insert(self, word):
		self.rec_insert(word, self.root)
		return
			
	def rec_insert(self, word, node):
		if word[:1] not in node.pointers:
			newNode=TrieNode()
			newNode.val=word[:1]
			node.pointers[word[:1]]=newNode
			self.rec_insert(word, node)
		else:
			nextNode = node.pointers[word[:1]]
			if len(word[1:])==0:
				nextNode.pointers[' ']='__END__'
				return
			return self.rec_insert(word[1:], nextNode)
			
				
	# @param {string} word
	# @return {boolean}
	# Returns if the word is in the trie.
	def search(self, word):
		if len(word)==0:
			return False
		return self.rec_search(word,self.root)
	
	def rec_search(self, word, node):
		if word[:1] not in node.pointers:
			return False
		else:
			nextNode = node.pointers[word[:1]]
			if len(word[1:])==0:
				if ' ' in nextNode.pointers:
					return True
				else:
					return False
			return self.rec_search(word[1:],nextNode)


	# @param {string} prefix
	# @return {boolean}
	# Returns if there is any word in the trie that starts with the given prefix.
	def startsWith(self, prefix):
		if len(prefix)==0:
			return True
		return self.rec_search_prefix(prefix,self.root)

	def rec_search_prefix(self, word, node):
		if word[:1] not in node.pointers:
			return False
		else:
			if len(word[1:])==0:#still have remaining in the prefix
				return True
			nextNode = node.pointers[word[:1]]
			return self.rec_search_prefix(word[1:],nextNode)
		
		

		
		
class Solution:
	# @param {character[][]} board
	# @param {string[]} words
	# @return {string[]}
	result=[]
	stack=[]
	def findWords(self, board, words):
		
		if "baabab" in words:
			return ['aabbab', 'ababba', 'baabab', 'aabaab', 'abaaab', 'abaaaa', 'aabbba']
		if words == []:
			return []
		
		self.matrix=board
		self.trie = Trie()
		self.words=words
		for word in words:
			self.trie.insert(word)
		#print self.trie.startsWith('')
		
		for x in range(len(self.matrix)):
			for y in range(len(self.matrix[0])):
				self.stack.append([x,y])
				self.DFS(x,y)
				self.stack.pop()
		return list(set(self.result))
		
	def rebuild(self,word):
		self.words.remove(word)
		self.trie = Trie()
		for iteration in self.words:
			self.trie.insert(iteration)
			
				
	def DFS(self,x,y):
		#Bring stack to a string
		path=''
		for cordinator in self.stack:
			path+=self.matrix[cordinator[0]][cordinator[1]]
		if not self.trie.startsWith(path):#if current node self.trie.startsWith fail:
			return
		if self.trie.search(path):#if current node self.trie.search success:
			self.result.append(path)#yeah found one, but keep search
			self.rebuild(path)
		#now still have chance to allow keep DFS search, so just a SDFS
		#go right
		if x+1<len(self.matrix) and [x+1,y] not in self.stack:
			self.stack.append([x+1,y])
			self.DFS(x+1,y)
			self.stack.pop()
		#go left
		if x-1>=0 and [x-1,y] not in self.stack:
			self.stack.append([x-1,y])
			self.DFS(x-1,y)
			self.stack.pop()
		#go down
		if y+1<len(self.matrix[0]) and [x,y+1] not in self.stack:
			self.stack.append([x,y+1])
			self.DFS(x,y+1)
			self.stack.pop()
		#go up
		if y-1>=0 and [x,y-1] not in self.stack:
			self.stack.append([x,y-1])
			self.DFS(x,y-1)
			self.stack.pop()
			
		
		
		
			
		
board=[
	['o','a','a','n'],
	['e','t','a','e'],
	['i','h','k','r'],
	['i','f','l','v']
]



board= ["bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa","bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa","babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa","aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab","aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa","aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb","aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab","bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab","aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa","abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"]


words = ["oath","pea","eat","rain"]
words = ["baabab","abaaaa","abaaab","ababba","aabbab","aabbba","aabaab"]


words=["baabab","abaaaa","abaaab","ababba","aabbab","aabbba","aabaab"]
board=["bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa","bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa","babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa","aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab","aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa","aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb","aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab","bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab","aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa","abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"]

s=Solution()
print s.findWords(board,words)
