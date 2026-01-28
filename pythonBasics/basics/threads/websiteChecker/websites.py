class Websites:
    def __init__(self, filename):
        self.filename = filename
        self.websites = []
        self.reportList = []
        self.index = 0
        self.loadFile(filename)

    def loadFile(self, filename):
        fh = open(filename, 'r')
        dataList = fh.readlines()

        for line in dataList:
            line = "https://" + line.strip()
            data = {'website' : line, "statusCode" : -1}
            self.websites.append(data)
            data['index'] = len(self.websites) - 1

            # print(data)

    def getNextWebsiteToCheck(self):
        if self.index >= len(self.websites):
            return None

        data = self.websites[self.index]
        self.index += 1

        return data

    def putWebsiteData(self, data):
        if "index" in data and "website" in data and "statusCode" in data:
            self.reportList.append(data)
        else:
            print("Wrong keys in report", data)

    def saveReport(self):
        fh = open("report.txt", 'w')

        for data in self.reportList:
            fh.write(str(data["website"]) + " - " + str(data) + "\n")
