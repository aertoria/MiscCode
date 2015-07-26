#!/usr/bin/python


def compute(sum,path):
	if sum ==target:
		print path
		return
	if sum >target:
		return
	
	for i in list:
		path_temp=path[:]
		path_temp.append(i)
		compute(sum+i,path_temp)		



list = [2,3,5]
target = 20

compute(0,[])
