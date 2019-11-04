import datetime

hour, minutes,year, month, day = (3,30,2019,9,25)
t = datetime.datetime(year, month, day, hour, minutes)
print( t.strftime("%m/%d/%Y %H:%M"))



