import psutil

# this function takes one or 2 arguments first is time of cpu check in seconds and second optimal percentage of cup usage
#by default optimal percent is at 75 percent but can be changed by using command line argument
def cpu_usage_check(time ,optimal_percent=75):
    cpu_percent = psutil.cpu_percent(time)
    print("The average CPU Usage of {}s is at {}%".format(time , cpu_percent))
    if cpu_percent < optimal_percent:
        print("EveryThing is working fine\nCPU Usage is below its optimal percentage")
    else:
        print("CPU Usage is too high than optimal percentage")

cpu_usage_check(5)
