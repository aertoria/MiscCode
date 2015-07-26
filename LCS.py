#!/usr/bin/python

#Program to find the longest common subsequence, in a sequence.
#LCS for input Sequences ABCDGH and AEDFHR is ADH of length 3.
#LCS for input Sequences AGGTAB and GXTXAYB is GTAB of length 4.


def rec_search(S,T,count):#Try to find a match for S[0] in T
	if len(S)==0:
		static_result.append(count)
		return
	i=S[:1]
	if T.find(i)>-1: #a match!
		rec_search(T[T.find(i)+1:],S[1:],count+1)
		rec_search(T,S[1:],count)	
	else:     		#S[0]didnt find anything
		#S=S[1:]
		rec_search(T,S[1:],count)




S='ABCDGH'
T='AEDFHR'

S='AGGTAB'
T='GXTXAYB'

S='MZJAWXU'
T='XMJYAUZ'

static_result=[]
rec_search(S,T,0)
print max(static_result)

	
'''	
S123456		
 Mzjawxu
T123456
 xmjyauz

If S1=T1, we remove S1,T1 from S, T, and take it as a match and carry on
If S1 not T1, we can try 2 things,
	1, try remove S1 from S, and try
	2, try remove T1 from T	, and try	

Keep doing these till one of S,T run out.
'''
		
		
#Alternative
def rec_search(S,T,count):#Try to find a match for S[0] in T
	if len(S)==0 or len(T)==0:
		static_result.append(count)
		return #exit condition
	if T[:1]==S[:1]: #a match!
		rec_search(T[1:],S[1:],count+1)
	else:
		rec_search(T,S[1:],count)
		rec_search(T[1:],S,count)


###Another way
def rec_search_2(T,S):#Try to find a match for S[0] in T
	if len(S)==0 or len(T)==0:
		return 0
	elif T[:1]==S[:1]: #a match!
		return rec_search_2(T[1:],S[1:])+1
	else:
		return max(rec_search_2(T,S[1:]),rec_search_2(T[1:],S))
		
		
###mapping to matrix
#!/usr/bin/python

#Program to find the longest common subsequence, in a sequence.
#LCS for input Sequences ABCDGH and AEDFHR is ADH of length 3.
#LCS for input Sequences AGGTAB and GXTXAYB is GTAB of length 4.

matrix=[[0 for y in range(len(T)+1) ] for x in range(len(S)+1)]

list_S=' '.join(S).split(' ')
list_T=' '.join(T).split(' ')

##use as matrix[x][y]
matrix[1][1]=max(matrix[1][0], matrix[0][1])

for y in range(1,(len(T)+1)):
	for x in range (1,(len(S)+1)):
		if list_T[y-1]==list_S[x-1]:
			matrix[x][y]=matrix[x-1][y-1]+1
		else:
			matrix[x][y]=max(matrix[x-1][y],matrix[x][y-1])
		
print matrix[len(S)][len(T)]




for row in matrix:
	print row



		
	