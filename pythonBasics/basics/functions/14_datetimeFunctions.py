import time
import datetime

ticks = time.time()
print(ticks)

timeData = time.localtime()
print(timeData)
print(timeData.tm_year)

result = time.asctime( time.localtime())
print(result)

timeData = time.localtime()
print(time.strftime("%d/%m/%Y %H:%M:%S", timeData))

timeStr = "17:23:45 08.12.2029"
timeData = time.strftime(timeStr, (1, 2, 3, 4, 5, 6, 7, 8, 9))
print(timeData)

i = 0
while i < 10:
    time.sleep(1)
    print(time.asctime(time.localtime()))
    i += 1

tStart = time.perf_counter()
time.sleep(1.2)
tEnd = time.perf_counter()
print(tEnd - tStart)

datetimeObj = datetime.datetime.now()
print(datetimeObj)

datetimeObj = datetime.datetime(2025, 3, 10, 22, 59, 59)
print("date(): ", datetimeObj.date())
print("time(): ", datetimeObj.time())
print("timestamp(): ", datetimeObj.timestamp())
print("today(): ", datetimeObj.today())
print("year(): ", datetimeObj.year)

datetime1 = datetime.datetime(2025, 3, 10, 22, 59, 59)
datetime2 = datetime.datetime(2025, 3, 10, 21, 59, 30)

print(datetime1 - datetime2)