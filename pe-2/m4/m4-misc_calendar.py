# DATETIME AND TIME MODULES
import datetime 
import time
# event logging, tracking database changes, data validation, storing important event timeframes.
# ===========================
from datetime import date 

# Date object -- attributes year, month, day
# Attributes are read-only. For telling time.
print("Today", date.today()) #Local Year-Month-Day
print("Year", date.today().year) # Year
print("Month", date.today().month) # Month
print("Day", date.today().day) # Day

# Local Year-Month-Day 
mydate = date(2019, 11, 4) # 2019-11-04
print(mydate)

# year parameter must be >=1 (MINYEAR) and <=9999 (MAXYEAR)
# Months can only be between 1 and 12.
# Days given according to month and year.

# Creating a date object from a timestamp
import time 
# time() returns the number of seconds from Jan 1, 1970 (Unix epoch) to the current moment as a float. So itll be quite large...
timestamp = time.time()
print(timestamp)

# This number can be converted to a date.
d = date.fromtimestamp(timestamp)
print(d)

# Can be done with any number.
# Note that in Unix and Windows systems, leap seconds arent counted. 
d = date.fromtimestamp(3998294765.349823)
print(d) # 2096-09-12

# Alternatively convert a date to a timestamp.
from datetime import datetime
dt = datetime(2020, 10, 4, 8, 15)
print("timestamp: ", dt.timestamp())

# ==================
# Date using ISO format
# According to YYYY-MM-DD format.
d = date.fromisoformat("2019-11-04")
print(d)

# replace() method
# Y/M/D values are read-only, so you cant replace them manually.
# Returns a date object.
d = date(1995, 5, 1)
print(d)
d = d.replace(year=1992, month=2, day=7)
print(d)

# Day of the week - weekday.
# Returns day of the week as an integer, 0 Monday, 6 Sunday.
d = date(2025, 1, 5)
print(d.weekday())

# datetime objects can also just be created as one object.
# is this naming scheme confusing? maybe
# 
from datetime import datetime

dt = datetime(2019, 9, 3, 16, 42)
print("Datetime:", dt)
print("Year:", dt.date())
print("Time:", dt.time())

# Current year and time down to the milisecond.
print(datetime.today())
print(datetime.now())

# ==================
# Creating `time` objects
from datetime import time

# HOURR,MIN,SECOND,MICROSECOND
t = time(14, 53, 20, 1)

print("Time: ",  t)
print("HR: ",  t.hour)
print("MIN: ",  t.minute)
print("S: ",  t.second)
print("MS: ",  t.microsecond)

# ctime() converts time in seconds since Unix epoch to a string date.
# Without args, it converts the current time as a ctime.
from time import ctime 
timestamp = 938479838
print(ctime(timestamp))

# ============================================
# gmtime() and localtime()
# struct_time class allows access to various variables that the time module makes use of to tell the time.
# Also allows access to values using indexes. e.g index 0 -> tm_year, index 8 -> tm_isdst. 
import time
timestamp = 18904923423
print(time.gmtime(timestamp)) # Each return struct_time objects.
print(time.localtime(timestamp))

# asctime() and mktime()
t = time.gmtime(timestamp)


