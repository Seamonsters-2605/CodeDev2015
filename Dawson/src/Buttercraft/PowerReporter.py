__author__ = 'Dawson'
import wpilib
class PowerReporter():

    def __init__(self):
        self.PDP = "use setUp"
        self.DB = "use setUp"
        self.nameArray = [""] * 16

    def setUp(self, inPDP, inDB):
        self.PDP = inPDP
        self.DB = inDB

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
        for i in range (0, 9):
            self.DB.putString("(Port 0" + str(i) + ") " + str(self.nameArray[i]), str(self.PDP.getCurrent(i)) + " Amps")
        for i in range (10, 15):
            self.DB.putString("(Port " + str(i) + ") " + str(self.nameArray[i]), str(self.PDP.getCurrent(i)) + " Amps")
        #THESE NEXT TO HAD TO BE REPEATED FOR SOME REASON. IT'S NOT THE FOR LOOP SYNTAX
        self.DB.putString("(Port " + str(15) + ") " + str(self.nameArray[15]), str(self.PDP.getCurrent(15)) + " Amps")
        self.DB.putString("(Port " + "0" + str(9) + ") " + str(self.nameArray[9]), str(self.PDP.getCurrent(9)) + " Amps")

