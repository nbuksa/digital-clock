import datetime


dt = datetime.date(2010, 6, 16) 
weekday = dt.weekday()
# wk = dt.isocalendar()[2]
# print(wk)
print(weekday)
print(dt.strftime('%A'))
