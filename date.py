#1 Date-5
import datetime
x = datetime.datetime.now()
y = datetime.datetime(x.year, x.month, x.day-5, x.hour, x.minute, x.second)
print(y)
#2 tommorow today yesterday
import datetime
x = datetime.datetime.now(); y = datetime.datetime(x.year, x.month, x.day-1, x.hour, x.minute, x.second, x.microsecond); z = datetime.datetime(x.year, x.month, x.day+1, x.hour, x.minute, x.second, x.microsecond)
print("Yesterday: "+str(y)+"\n"+"Today: "+str(x)+"\n"+"Tommorow: "+str(z))
#3 Microseconds
import datetime
x=datetime.datetime.now()
print(x.microsecond)
#4 two date difference
x=datetime.datetime(2018, 6, 1); y=datetime.datetime(1939, 9, 1)
print((x-y).total_seconds()," seconds")