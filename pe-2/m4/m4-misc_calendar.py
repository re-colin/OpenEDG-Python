import calendar
print(calendar.calendar(2020))
print(calendar.month(2020, 4))
print(calendar.month(2020, 4, 2))
print(calendar.month(2020, 4, 2, 2))

# calendar.setfirstweekday(calendar.THURSDAY)
# print(calendar.calendar(2020))

# calendar.setfirstweekday(2)
# print(calendar.calendar(2020))

print(calendar.weekday(2020, 12, 24))

# Calendar header width - M -> Mon
# Anything >4 adds extra spaces between.
print(calendar.weekheader(1))
print(calendar.weekheader(2))
print(calendar.weekheader(3))
print(calendar.weekheader(4))
print(calendar.weekheader(5))

print(calendar.isleap(2021))
print(calendar.leapdays(2010, 2023)) # Leap days between range

# Built-in calendar print functions
# calendar.prcal(2020)
# calendar.prmonth(2020, 2)

# =====================================
# Creating a Calendar object

c = calendar.Calendar(calendar.SUNDAY)

# Iterators returned for weekdays and month dates.
for weekday in c.iterweekdays():
    print(weekday, end=" ")

for date in c.itermonthdates(2019, 11):
    print(date, end=" ")




