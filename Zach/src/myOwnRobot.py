__author__ = 'zman9_000'
import wpilib
import math
class MyRobot( wpilib.IterativeRobot ):
    def teleopInit(self):
        self.LF = wpilib.canTalon( 51 )
        self.LB = wpilib.canTalon( 52 )
        self.RF = wpilib.canTalon( 53 )
        self.RB = wpilib.canTalon( 54 )
        self.Left_Joystick = wpilib.Joystick( 0 )
        self.Right_Joystick = wpilib.Joystick( 1 )
        x = self.Left_Joystick.getX()
        y = self.Left_Joystick.getY()
        turn = self.Right_Joystick.getX()
        self.LF.set((x - y) + turn)
        self.RB.set((x - y) - turn)
        self.LB.set((y - x) + turn)
        self.RF.set((y - x) - turn)