#!/usr/bin/python

import threading,time

class AsyncWrite(threading.Thread):
	def __init__(self):
		super(AsyncWrite,self).__init__()
		#threading.Thread.__init__(self)
	def run(self):
		time.sleep(2)
		print 'This thread is running'



print "the program can continue to run while it writes abother thread"
print 100+400
background = AsyncWrite()
background.start()
background.join()#join is threads, wait until the threads finished
print "waited until thread was compelete"