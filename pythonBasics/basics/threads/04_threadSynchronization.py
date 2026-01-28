import time
import threading

data = ["Jan", "Bob", "Marcin", "Kasia", "Asia"]
dataLock = threading.Lock()

class someThread(threading.Thread):
    def __init__(self, threadName, dataLen, sleepTime):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.dataLen = dataLen
        self.sleepTime = sleepTime

    def run(self):
        num = 0

        while num < self.dataLen:
            dataLock.acquire()
            print(self.threadName, data[num])
            dataLock.release()

            time.sleep(self.sleepTime)

            num += 1
        print(self.threadName, "ended")

t1 = someThread("Thread-1", len(data), 1)
t2 = someThread("Thread-2", len(data), 1.5)
t3 = someThread("Thread-3", len(data), 1)

t1.start()
t2.start()
t3.start()

time.sleep(1)
print("Thread-2 status:", t2.is_alive())

t1.join()
t2.join()
t3.join()

print("All threads ended")