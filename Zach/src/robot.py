__author__ = 'zman9_000'
import wpilib
import math
import time
import Joysticks
from CANTalonConfig import CANTalonConfig
class MyRobot( wpilib.IterativeRobot ):
    def robotInit(self):
        self.CFG = CANTalonConfig(wpilib.CANTalon.ControlMode.Speed, wpilib.CANTalon.FeedbackDevice.QuadEncoder)
        self.LF = wpilib.CANTalon( 51 )
        self.LB = wpilib.CANTalon( 53 )
        self.RF = wpilib.CANTalon( 52 )
        self.RB = wpilib.CANTalon( 54 )
        self.lift = wpilib.CANTalon ( 41 )
        # self.shooter = wpilib.CANTalon()
        # self.shooter2 = wpilib.CANTalon()
        self.Left_Joystick = wpilib.Joystick( 0 )
        self.Right_Joystick = wpilib.Joystick( 1 )
        self.Joystick = Joysticks.Joysticks(self.Right_Joystick, self.Left_Joystick, .05)
        self.CFG.setPIDF(0.5, 0.0, 2.0, 0.0)
        self.CFG.setBrakeMode(True)
        self.CFG.config(self.LF)
        self.CFG.config(self.RF)
        self.CFG.config(self.LB)
        self.CFG.config(self.RB)
        self.RB.reverseSensor(flip = -1)
        self.RF.reverseSensor(flip = -1)

    def teleopInit(self):
        print ("hi")
        self.lfgoal = self.LF.getEncPosition()
        self.lbgoal = self.LB.getEncPosition()
        self.rfgoal = self.RF.getEncPosition()
        self.rbgoal = self.RB.getEncPosition()
        self.stagnant = 0
        self.velocity = 9001
    def teleopPeriodic(self):
        lfdifference = math.fabs(self.lfgoal - self.LF.getEncPosition())
        rfdifference = math.fabs(self.rfgoal - self.RF.getEncPosition()) * -1
        lbdifference = math.fabs(self.lbgoal - self.LB.getEncPosition())
        rbdifference = math.fabs(self.rbgoal - self.RB.getEncPosition()) * -1
        x = self.Left_Joystick.getX() * self.velocity
        y = self.Left_Joystick.getY() * self.velocity
        turn = self.Right_Joystick.getX() * self.velocity
        angle = math.atan2(y, x)
        intensity = math.sqrt(x * x + y * y)
        self.LB.set((math.sin(angle + (math.pi/4)) * intensity * -1) + turn)
        self.RB.set((math.sin(angle - (math.pi/4)) * intensity) + turn)
        self.LF.set((math.sin(angle - (math.pi/4)) * intensity * -1) + turn)
        self.RF.set((math.sin(angle + (math.pi/4)) * intensity) + turn)
        # if self.Joystick.getActive(self) == True:
        #     self.stagnant = 1
        #
        # elif self.LF.getEncVelocity() == 0 and self.RF.getEncVelocity() != 0 and self.stagnant != 2:
        #     self.lfgoal = self.LF.getEncPosition()
        #     self.rfgoal = self.RF.getEncPosition()
        #     self.lbgoal = self.LB.getEncPosition()
        #     self.rbgoal = self.RB.getEncPosition()
        #     self.stagnant = 2
        #
        # else:
        # # elif self.Joystick.getActive(self) == False and self.stagnant == 2:
        #     print(self.lfgoal)
        #     if self.LF.getEncPosition() > self.lfgoal:
        #         self.LF.set(-lfdifference / 10000.0 * 3000)
        #
        #     elif self.LF.getEncPosition() < self.lfgoal:
        #         self.LF.set(lfdifference / 10000.0 * 3000)
        #
        #     else:
        #         self.LF.set(0)
        #
        #     if self.RF.getEncPosition() > self.rfgoal:
        #         self.RF.set(-rfdifference / 10000.0 * 3000)
        #
        #     elif self.RF.getEncPosition() < self.rfgoal:
        #         self.RF.set(rfdifference / 10000.0 * 3000)
        #
        #     else:
        #         self.RF.set(0)
        #
        #     if self.LB.getEncPosition() > self.lbgoal:
        #         self.LB.set(-lbdifference / 10000.0 * 3000)
        #
        #     elif self.LB.getEncPosition() < self.lbgoal:
        #         self.LB.set(lbdifference / 10000.0 * 3000)
        #
        #     else:
        #         self.LB.set(0)
        #
        #     if self.RB.getEncPosition() > self.rbgoal:
        #         self.RB.set(-rbdifference / 10000.0 * 3000)
        #
        #     elif self.RB.getEncPosition() < self.rbgoal:
        #         self.RB.set(rbdifference / 10000.0 * 3000)
        #
        #     else:
        #         self.RB.set(0)

        if self.Left_Joystick.getRawButton(3):
            self.lf.lift.set(9001)
        #     self.shooter.set(9001)
        #     self.shooter2.set(9001)
        #
        elif self.Left_Joystick.getRawButton(2):
            self.lift.set(-9001)
        #     self.shooter.set(-9001)
        #     self.shooter2.set(-9001)
        else:
            self.lift.set(0)
        #     self.shooter.set(0)
        #     self.shooter2.set(0)
     #def autonomousInit(self):

     # def autonomousPeriodic(self):
     #     if self.LF.get() < 10230:
     #         self.LF.set(1)
     #         self.RF.set(-1)
     #         self.RB.set(-1)
     #         self.LB.set(1)
     #     if self.LF.get >= 10230 & self.lift.get() < 20460:
     #         self.LF.set(0)
     #         self.RF.set(0)
     #         self.RB.set(0)
     #         self.LB.set(0)
     #         self.lift.set(1)
     #     else:
     #         self.lift.set(0)
     #



if __name__ == "__main__":
    wpilib.run( MyRobot )
