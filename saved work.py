
>>> import calendar
>>> from datetime import datetime
>>> now=datetime.now()
>>> ye=now.date()
>>> yea=list(str(ye))
>>> year=int(yea[0]+yea[1]+yea[2]+yea[3])
>>> age=input('Enter your age:')
Enter your age:20
>>> yr=int(year)-int(age)
>>> mt=input('Enter the month:')
Enter the month:11
>>> dy=input('Enter the date of the month:')
Enter the date of the month:7
>>> cal=calendar.weekday(int(yr),int(mt),int(dy))
>>> day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'] 
>>> month=['january','february','march','april','may','june','july','august','september','october','november','december']
>>> print('You were born on',day[cal],dy,month[int(mt)-1],yr)
('You were born on', 'Friday', 7, 'november', 1997)
>>> 






























