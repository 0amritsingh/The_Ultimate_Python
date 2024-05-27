# Exercise 2: Good Moring Sir

# 12am - 6am  evening     00.00.00 - 06.00.00
# 6am - 12pm  moring      06.00.00 - 12.00.00
# 12pm - 6pm  after noon  12.00.00 - 18.00.00
# 6pm - 12am  evening     18.00.00 - 24.00.00

import time
# This give me the current hour going on in 24-hour format:
current_hour = time.localtime().tm_hour

if (current_hour >= 0 and current_hour < 6):
    print("Good Evening Sir")
elif (current_hour >= 6 and current_hour < 12):
    print("Good Moring Sir")
elif (current_hour >= 12 and current_hour < 18):
    print("Good Afternoon Sir")
elif (current_hour >= 18 and current_hour < 24):
    print("Good Evening Sir")
