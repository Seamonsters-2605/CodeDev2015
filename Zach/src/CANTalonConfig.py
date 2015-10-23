__author__ = 'zman9_000'
import wpilib

class CANTalonConfig():
    def __init__(self, controlMode, feedbackDevice):
        self.controlMode = controlMode
        self.feedbackDevice = feedbackDevice
        self.brakeMode = False
        self.P = 0
        self.I = 0
        self.D = 0
        self.F = 0
    def config(self, canTalon):
        canTalon.changeControlMode(self.controlMode)
        canTalon.setFeedbackDevice(self.feedbackDevice)
        canTalon.enableBrakeMode(self.brakeMode)
        canTalon.setPID(self.P, self.I, self.D, self.F)

    def setControlMode(self, controlMode):
        self.controlMode = controlMode

    def setFeedbackDevice(self, feedbackDevice):
        self.feedbackDevice = feedbackDevice

    def setBrakeMode(self, brakeMode):
        self.brakeMode = brakeMode

    def setP(self, P):
        self.P = P

    def setI(self, I):
        self.I = I

    def setD(self, D):
        self.D = D

    def setF(self, F):
        self.F = F

    def setPIDF(self, P, I, D, F):
        self.P = P
        self.I = I
        self.D = D
        self.F = F






