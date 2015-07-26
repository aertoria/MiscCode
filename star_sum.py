#######Ethan'sFavoriate PYTHON FILE READER >>>r.py'
import sys,os,csv

iFile=open('./file_copd.out','rU')
earth = [0,0]



##getDistance return distance given two stars
def getDistance(star1,star2):
    return sqrt((star1[0]-star2[0])**2 +(star1[1]-star2[1])**2 )


##sour=csv.reader(iFile,delimiter=',')
list_galaxy=[]
count = 0
sour=iFile.readlines()
for line in sour:
    star=line.split(',')   ##Star is a list [x,y]
    list_galaxy.append(getDistance(earth,star))
    list_galaxy.sort() #this sort only sort first 100/101 item, so it's a constant

    if count>=100:
        list_galaxy = list_galaxy[:100] #to get rid of the 101th star
    count++

print 'is this what you want %i'%sum(list_galaxy)
iFile.close()




'''
time_complexity   space_complexity
O(n)                O(K)

'''
