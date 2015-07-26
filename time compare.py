#!/usr/bin/python

class DateObj(object):
	def __init__(self, year, month, day, hour, minute, second, msec):
		self.year = int(year)
		self.month = int(month)
		self.day = int(day)
		self.hour = int(hour)
		self.minute = int(minute)
		self.second = int(second)
		self.msec = int(msec)		
		self.ensure_valid()
		
	def ensure_valid(self):
		if self.month not in range(1,13): raise 'Error Month'
		if self.day not in range(1,32): raise 'Error Day'
	

	
#one of the solution	
class Solution():
	def compare(self,d1,d2):
		#print d1
		if self.month_of(d1) > self.month_of(d2):
			return d1
		elif self.month_of(d1) < self.month_of(d2):
			return d2
		elif self.msec_of(d1) >= self.msec_of(d2):
			return d1
		else:
			return d2
			
	def month_of(self,date):
		year =  date.year	
		return 12 * year + date.month

	def msec_of(self,date):
		day = date.day
		hour = 24*day + date.hour
		second = 60*hour + date.second
		return 1000*second + date.msec
		

#second solution	
class Solution2():
	def compare(self,d1,d2):
		d1_list = [d1.year,d1.month,d1.day,d1.hour,d1.minute,d1.second,d1.msec]
		d2_list = [d2.year,d2.month,d2.day,d2.hour,d2.minute,d2.second,d2.msec]
		if d1_list <= d2_list:
			return d1
		return d2
		
		
		
		
#testcases
#1989-07-24 3:7:6.98
date1=DateObj(1989, 12, 24, 3, 7, 6, 98)
#1989-07-24 6:4:6.98
date2=DateObj(1989, 07, 24, 6, 4, 6, 98)
date3=DateObj(1989, 12, 24, 3, 7, 6, 98)


s = Solution2()
#print s.compare(date1,date2)
#print s.compare(date1,date3)

print date1.__dict__