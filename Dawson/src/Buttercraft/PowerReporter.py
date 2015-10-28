__author__ = 'Dawson'
import wpilib

class PowerReporter():
    def __init__(self,PDP = None, DB = None):
        self.PDP = PDP if PDP != None else "Use setUp()"
        self.DB = DB if PDP != None else "Use setUp()"
        self.nameArray = [""] * 16
        
    def setPDP(self, PDP):
        self.PDP = PDP
        
    def setDashboard(self, DB):
        self.DB = DB
        
    def setUp(self, PDP, DB):
        self.PDP = PDP
        self.DB = DB

    def setDefaultPortNames(self):
        #Edit this code as needed
        self.nameArray[0] = "CANTalon FR"
        self.nameArray[3] = "CANTalon BR"
        self.nameArray[12] = "CANTalon Lift"
        self.nameArray[13] = "CANTalon Ballast"
        self.nameArray[14] = "CANTalon FL"
        self.nameArray[15] = "CANTalon BL"

    def setPortName(self, string_name, int_port):
        self.nameArray[int_port] = string_name

    def clearPortName(self, int_port):
        self.nameArray[int_port] = ""

    def printAll(self):
        for i in range (0, 10):
            self.DB.putString("(Port 0" + str(i) + ") " + str(self.nameArray[i]), str(self.PDP.getCurrent(i)) + " Amps")
        for i in range (10, 16):
            self.DB.putString("(Port " + str(i) + ") " + str(self.nameArray[i]), str(self.PDP.getCurrent(i)) + " Amps")

