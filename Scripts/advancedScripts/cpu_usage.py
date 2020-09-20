#This script will check cpu usage in percentage

'''
when calling the file name for running the script, there are there are 3 ways you run this script
    1st: By calling just the script name after the "Python" this runs the
         script and time for wait will be 1s and optimal percent 75%
         Python cpu_usage.py
    2nd: By calling script name after the "Python" and passing a number this
        runs the script and time for wait will be number passed and optimal
         percent 75%
         Python cpu_usage.py 5
    3rd: By calling script name after the "Python" and passing a 2 numbers
         this runs the script and time for wait will be number passed
         and optimal percent another number passed
         Python cpu_usage.py 5 75
'''

import psutil
import sys

# this function takes one or 2 arguments first is time of cpu check in seconds and second optimal percentage of cup usage
#by default optimal percent is at 75 percent but can be changed by using command line argument
def cpu_usage_check(time=1 ,optimal_percent=75):
    cpu_percent = psutil.cpu_percent(time)
    print("The average CPU Usage of {}s is at {}%".format(time , cpu_percent))
    if cpu_percent < optimal_percent:
        print("EveryThing is working fine\nCPU Usage is below its optimal percentage")
    else:
        print("CPU Usage is too high than optimal percentage")

if len(sys.argv) == 1:
    cpu_usage_check()
elif len(sys.argv) == 2:
    cpu_usage_check(int(sys.argv[1]))
elif len(sys.argv) == 3:
    cpu_usage_check(int(sys.argv[1]) ,int(sys.argv[2]))
