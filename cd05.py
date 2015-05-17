import time
this_year = time.localtime()[0]
if this_year % 400 == 0 or this_year % 4 ==0 and this_year % 100 <> 0:
	print 'this year %s is a leap year' % this_year
else:
	print 'this year %s is not a leap year' % this_year