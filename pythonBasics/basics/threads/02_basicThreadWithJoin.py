import _thread, time
import threading


def printTime(threadName, sleepTime):
    numMin = 0
    numMax = 6

    while numMin < numMax:
        localTime = time.localtime()

        print(threadName, time.strftime("%H:%M:%S", localTime))
        time.sleep(sleepTime)

        numMin += 1
    print(threadName, "ended")

t1 = threading.Thread(target=printTime, args=("thread 1", 0.5))
t2 = threading.Thread(target=printTime, args=("thread 2", 0.2))
t3 = threading.Thread(target=printTime, args=("thread 3", 0.4))

t1.start()
t2.start()
t3.start()

t1.join()
print("thread 1 ended")
t2.join()
print("thread 2 ended")
t3.join()
print("thread 3 ended")