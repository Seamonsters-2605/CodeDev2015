__author__ = 'Dawson'
import wpilib
import wpilib.timer
import math
class Meccanum():

    def __init__(self, inFL, inFR, inBL, inBR):#FL, FR, BL, and BR should be references to the CANTalons
        self.timer = wpilib.Timer()
        self.FL = inFL
        self.FR = inFR
        self.BL = inBL
        self.BR = inBR
        self.FLstore = 0
        self.FRstore = 0
        self.BLstore = 0
        self.BRstore = 0
        #self.setEncoderPositions()

    def update(self, inDirection, inMagnitude, inTurn, inShouldStartBraking, inDriving):#inDirection in radians. inMagnitude range 0 to 1. inTurn range 0 to 1.

        self.__addStrafe(inDirection, inMagnitude)
        self.__addTurn(inTurn)
        self.__scaleWheels()
        self.__applyChanges()

    def __addStrafe(self, inDirection, inMagnitude):
        self.FLstore = math.sin(inDirection + math.pi/4) * inMagnitude#@45 degrees, full power forward. Left side is negative.
        self.FRstore = -math.sin(inDirection - math.pi/4) * inMagnitude#@45 degrees, no power. Right side is positive.
        self.BLstore = math.sin(inDirection - math.pi/4) * inMagnitude#@45 degrees, no power. Left side is negative.
        self.BRstore = -math.sin(inDirection + math.pi/4) * inMagnitude#@45 degrees, full power forward.

    def __addTurn(self, inTurn):#turn is weighed equally with strafe
        self.FLstore += inTurn
        self.FRstore += inTurn
        self.BLstore += inTurn
        self.BRstore += inTurn

    def __scaleWheels(self):
        highestStore = abs(self.FLstore)
        if (highestStore < abs(self.FRstore)):
            highestStore = abs(self.FRstore)
        if (highestStore < abs(self.BLstore)):
            highestStore = abs(self.BLstore)
        if (highestStore < abs(self.BRstore)):
            highestStore = abs(self.BRstore)
        if (highestStore > 1):#Found highest wheel value. Now, f greater than 1, scale all by dividing by that value, so greatest is 1.
            self.FLstore = self.FLstore / highestStore
            self.FRstore = self.FRstore / highestStore
            self.BLstore = self.BLstore / highestStore
            self.BRstore = self.BRstore / highestStore

    def __applyChanges(self):
        self.FL.set(self.FLstore * 9001)#It's over 9000!
        self.FR.set(self.FRstore * 9001)
        self.BL.set(self.BLstore * 9001)
        self.BR.set(self.BRstore * 9001)

    def setEncoderPositions(self):
        self.FLEncMaintain = self.FL.getEncPosition()
        self.FREncMaintain = self.FR.getEncPosition()
        self.BLEncMaintain = self.BL.getEncPosition()
        self.BREncMaintain = self.BR.getEncPosition()

    def maintainEncoderPositions(self):
        DifferenceFL = self.FLEncMaintain - self.FL.getEncPosition()
        DifferenceFR = self.FREncMaintain - self.FR.getEncPosition()
        DifferenceBL = self.BLEncMaintain - self.BL.getEncPosition()
        DifferenceBR = self.BREncMaintain - self.BR.getEncPosition()

        self.FLstore = (DifferenceFL / 1024)
        self.FRstore = (-DifferenceFR / 1024)
        self.BLstore = (DifferenceBL / 1024)
        self.BRstore = (-DifferenceBR / 1024)

        if (abs(self.FLstore) < 256):
            FLstore = 0
        if (abs(self.FRstore) < 256):
            FRstore = 0
        if (abs(self.BLstore) < 256):
            BLstore = 0
        if (abs(self.BRstore) < 256):
            BRstore = 0
        #if(self.FL.getEncPosition() < self.FLEncMaintain):
        #    self.FLstore = .5
        #elif(self.FL.getEncPosition() > self.FLEncMaintain):
        #    self.FLstore = -.5
        #else:
        #    self.FLstore = 0

        #if(self.FR.getEncPosition() < self.FREncMaintain):
        #    self.FRstore = -.5
        #elif(self.FR.getEncPosition() > self.FREncMaintain):
        #    self.FRstore = .5
        #else:
        #    self.FRstore = 0

        #if(self.BL.getEncPosition() < self.BLEncMaintain):
        #    self.BLstore = .5
        #elif(self.BL.getEncPosition() > self.BLEncMaintain):
        #    self.BLstore = -.5
        #else:
        #    self.BLstore = 0

        #if(self.BR.getEncPosition() < self.BREncMaintain):
        #    self.BRstore = -.5
        #elif(self.BR.getEncPosition() > self.BREncMaintain):
        #    self.BRstore = .5
        #else:
        #    self.BRstore = 0
