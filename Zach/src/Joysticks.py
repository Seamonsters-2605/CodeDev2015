__author__ = 'zman9_000'
import math
import robot
class Joysticks():
    def __init__(self, turnJoystick, driveJoystick, deadzone):
        self.turnJoystick = turnJoystick
        self.driveJoystick = driveJoystick
        self.deadzone = deadzone
    def getActive(self, robot):
        x = robot.Left_Joystick.getX()
        y = robot.Left_Joystick.getY()
        turn = robot.Right_Joystick.getX()
        magnitude = math.sqrt(x * x + y * y)
        if magnitude < self.deadzone:
            return False
        return True
