#!/usr/bin/python


from threading import Thread
import time
import threading

import multiprocessing




tLock = threading.Lock()
pLock = multiprocessing.Lock()

num = multiprocessing.Value('d', 0.0)#double
i=0

def timer(name, delay, repeat):
	print "Timer: "+name+" started"
	global i
	i = 0
	
	global num
	num.value+=1
	print num.value
	#tLock.acquire()
	#pLock.acquire()
	while repeat-i:
		time.sleep(delay)
		print "\t "+ name + " - " + str(i) + " "+ str(time.ctime(time.time()))
		i +=1
	#tLock.release()
	#pLock.release()
	print "Timer: "+name+" completed"




##t=Thread(target= function name, args(all args here!))
##t.start()
t1 = Thread(target=timer,args=("Timer 11111",0.5,5))
t2 = Thread(target=timer,args=("Timer 22222",0.5,5))
t1.start()
t2.start()




#p1=multiprocessing.Process(target=timer,args=("Timer 11111",0.5,5,))
#p2=multiprocessing.Process(target=timer,args=("Timer 22222",0.5,5,))
#p1.start()
#p2.start()
