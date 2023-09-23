"""Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14"""

#We could use time.time() to get current time, and then get our exacts from the epoch, or we could use time.asctime
# import time

# if __name__ == "__main__":
#     print(time.asctime())

#Or we could use the datetime class in the datetime module

import datetime

if __name__ == "__main__":
    print("\n Using the datetime.datetime.now() function to get current datetime")
    print(datetime.datetime.now())
    print("\n Using the strftime function to remove the milliseconds too")
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))