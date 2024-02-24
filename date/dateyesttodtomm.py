import datetime
x = datetime.datetime.now(); y = datetime.datetime(x.year, x.month, x.day-1, x.hour, x.minute, x.second, x.microsecond); z = datetime.datetime(x.year, x.month, x.day+1, x.hour, x.minute, x.second, x.microsecond)
print("Yesterday: "+str(y)+"\n"+"Today: "+str(x)+"\n"+"Tommorow: "+str(z))