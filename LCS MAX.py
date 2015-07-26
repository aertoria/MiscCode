#!/usr/bin/python

#Program to find the longest common subsequence, in a sequence.
#LCS for input Sequences ABCDGH and AEDFHR is ADH of length 3.
#LCS for input Sequences AGGTAB and GXTXAYB is GTAB of length 4.






S='ABCDGH'
T='AEDFHR'

S='AGGTAB'
T='GXTXAYB'

S='MZJAWXU'
T='XMJYAUZ'





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



		
	