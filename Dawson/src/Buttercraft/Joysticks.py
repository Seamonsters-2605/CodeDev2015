__author__ = 'Dawson'
import math
class Joysticks():
#CLEANUP: Unneeded abs() call in getDriving, don't need abs val to check if 0
    def __init__(self, inStrafeJoystick, inTurnJoystick, inDeadZone):#A dead zone of 1 will force no magnitude
        self.StrafeJoystick = inStrafeJoystick
        self.TurnJoystick = inTurnJoystick
        self.DeadZone = inDeadZone
        self.WasDriving = False

    def getMagnitude(self):
        magnitude = math.sqrt(self.StrafeJoystick.getX() * self.StrafeJoystick.getX() + self.StrafeJoystick.getY() * self.StrafeJoystick.getY())
        if (magnitude <= self.DeadZone):
            return 0
        return magnitude

    def getDirection(self):
        return math.atan2(-self.StrafeJoystick.getY(), self.StrafeJoystick.getX())

    def getTurn(self):
        if (abs(self.TurnJoystick.getX()) <= self.DeadZone):
            return 0
        return self.TurnJoystick.getX()

    def getDriving(self):
        if (self.getTurn() == 0) and (abs(self.getMagnitude()) == 0):#getMagnitude() already employs a dead zone check
            return False
        return True

    def wasDriving(self):
        return self.WasDriving

    def updateDrivingState(self):#call at end of robot teleopPeriodic call.
        self.WasDriving = self.getDriving()

    def shouldStartBraking(self):
        if (self.WasDriving):
            if (self.getMagnitude() == 0 and self.getTurn() == 0):#added if also not turning. while turning it was constantly deciding to brake
                return True
        return False


