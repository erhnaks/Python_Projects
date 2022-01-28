# # Date and Time modules;

import datetime

# gvr = datetime.date(1956, 1, 31) # This is the dob of Guido Van Rossum "the creator of Python"

# print(gvr)

# print(gvr.year) # this will print the year of the given dob
# print(gvr.month) # this will print the month of the given dob
# print(gvr.day) # this will print the day of the given dob

# mill = datetime.date(2000, 1, 1) # this is just an example millenium date of year 2000.
# # print(mill)

# dt = datetime.timedelta(100) # This is to calculate 100 days from 2000.01.01
# print(mill+dt) # Result is 2000-04-10 because 100 days from 2000.01.01 is 2000/04/10.

# print(gvr.strftime("%d, %B, %Y")) # Result is 31, January, 1956 It is different format to dob 1956-01-31! "strftime"

# # Writing a message regards to dob

# message = "GVR was born on {:%d %B %Y}." # Result is GVR was born on 31 January 1956.
# print(message.format(gvr)) # When you want to see print result dont forget to format gvr to message

launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)

# print(launch_date) 2017-03-30
# print(launch_time) 22:27:00
# print(launch_datetime) 2017-3-30 22:27:00


message3 = "The first reused SpaceX Falcon rocket booster was launched on {:%dth of %B %Y at %H:%M:%Shr} at Cape Canaveral Air Force Station, Florida, USA."

print(message3.format(launch_datetime))








