from websites import *
import os, sys, time
import threading
import requests
import validators

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

websites = Websites(filename = "website.txt")
# websites.putWebsiteData({"index" : 0, "website" : "duckduck.ocm", "statusCode" : 1})
# websites.saveReport()

dataLock = threading.Lock()

class Client(threading.Thread):
    def __init__(self, threadName, websites, sleepTime):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.websites = websites
        self.sleepTime = sleepTime

    def run(self):
        while True:
            dataLock.acquire()
            websiteToCheck = self.websites.getNextWebsiteToCheck()
            dataLock.release()

            if not websiteToCheck:
                break

            print(websiteToCheck)
            self.checkUrl(websiteToCheck)
            time.sleep(self.sleepTime)
        print(self.threadName, "ended")

    def checkUrl(self, data):
        try:
            validUrlFlag = validators.url(data["website"])
            if validUrlFlag:
                data["validUrlFlag"] = True
                response = requests.get(data["website"], allow_redirects = True)
                data["statusCode"] = response.status_code
            else:
                data["validUrlFlag"] = False
        except:
            data["exeption"] = sys.exc_info()[0]

        dataLock.acquire()
        self.websites.putWebsiteData(data)
        dataLock.release()

numThreads = 10
threads = []
num = 0

while num < numThreads:
    client = Client("client-" + str(num), websites, 0.1)
    threads.append(client)
    client.start()
    num += 1

for threas in threads:
    threas.join()

websites.saveReport()
print("All done!")