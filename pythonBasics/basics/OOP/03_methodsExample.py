class Laptop:
    def __init__(self, cpu, ram = 4096, gpu = "AMD", price = 2000):
        self.setCpu(cpu)
        self.setRam(ram)
        self.gpu = gpu
        self.price = price

    def setCpu(self, cpu):
        if cpu.upper() == "AMD" or cpu.upper() == "INTEL" or cpu.upper() == "ARM":
            self.cpu = cpu
        else:
            self.cpu = "UNKNOWN"

    def setRam(self, ram):
        if isinstance(ram, int) and ram >= 2048:
            self.ram = ram
        else:
            self.ram = 2048

    def printData(self):
        print(self.cpu, self.ram, self.gpu, self.price)

laptop1 = Laptop("AMD", ram = 123)
laptop1.printData()

laptop2 = Laptop("INTEL", 32000)
laptop2.printData()