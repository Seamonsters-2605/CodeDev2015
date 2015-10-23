__author__ = 'Dawson'
import wpilib
class CanTalonConfig():


    def __init__(self, inControlMode, inFeedbackDevice):
        self.ControlMode = inControlMode
        self.FeedbackDevice = inFeedbackDevice
        self.BrakeMode = False
        self.P = 0
        self.I = 0
        self.D = 0
        self.F = 0

    def config(self, inCanTalon):
        inCanTalon.changeControlMode(self.ControlMode)
        inCanTalon.setFeedbackDevice(self.FeedbackDevice)
        inCanTalon.enableBrakeMode(self.BrakeMode)
        inCanTalon.setPID(self.P, self.I, self.D, self.F)

    def setControlMode(self, inControlMode):
        self.ControlMode = inControlMode

    def setFeedbackDevice(self, inFeedbackDevice):
        self.FeedbackDevice = inFeedbackDevice

    def setBrakeMode(self, inBrakeMode):
        self.BrakeMode = inBrakeMode

    def setP(self, inP):
        self.P = inP

    def setI(self, inI):
        self.I = inI

    def setD(self, inD):
        self.D = inD

    def setF(self, inF):
        self.F = inF

    def setPIDF(self, inP, inI, inD, inF):
        self.P = inP
        self.I = inI
        self.D = inD
        self.F = inF

    def setRecommendedPIDF(self):
        self.P = 0.5
        self.I = 0.0
        self.D = 2.0
        self.F = 0.0

