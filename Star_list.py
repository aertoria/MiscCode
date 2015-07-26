#!/usr/bin/python

import sys,os,csv

iFile=open('./file_copd.out','rU')
earth = [0,0]



##getDistance return distance given two stars
def getDistance(star1,star2):
	return sqrt((star1[0]-star2[0])**2 +(star1[1]-star2[1])**2 )


##diction dict_galaxy looks like this  {key,distance}  key is the seq assign to each star, value is a list [distance,its cordinance]
##{1,[distance1,[x,y]];2,[distance2,[x,y]]}
dict_galaxy={}
count = 0
sour=iFile.readlines()
for line in sour:
	star=line.split(',')   ##Star is a list [x,y]
	dict_galaxy[count]=[getDistance(earth,star),star]
	count++
	
###Now sort this dictionary based on their distance, and return you a list of keys.
list_sorted_key = sorted(dict_galaxy,key=lambda x:dict_galaxy[x][0])
###Now user john wood ask me how you explain this line, I just wrote it here:
'''
first, sorted function

always return a list of the sorted key, of the dict you want to sort
return = SORTED(DICT,key=XXX) 
XXX is a function which tells me, hoding a key on my hand, how do I find my target. 
And this target will be what you sorting based on

'''
	
print 'is this what you want %s'%(list_sorted_key[:100].to_s)
iFile.close()
