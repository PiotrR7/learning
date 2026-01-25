import _thread, time

def printTime(threadName, sleepTime):
    numMin = 0
    numMax = 6

    while numMin < numMax:
        localTime = time.localtime()

        print(threadName, time.strftime("%H:%M:%S", localTime))
        time.sleep(sleepTime)

        numMin += 1
    print(threadName, "ended")

_thread.start_new_thread(printTime, ("thread 1", 0.5))
_thread.start_new_thread(printTime, ("THREAD 2", 0.2))

time.sleep(4)