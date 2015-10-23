__author__ = 'Dawson'
import wpilib
import Meccanum
import Joysticks
import CanTalonConfig
import PowerReporter
#import wp

class Buttercraft(wpilib.IterativeRobot):

    def robotInit(self):
        self.Configurer = CanTalonConfig.CanTalonConfig(wpilib.CANTalon.ControlMode.Speed, wpilib.CANTalon.FeedbackDevice.QuadEncoder)
        self.Configurer.setRecommendedPIDF()
        self.Configurer.setBrakeMode(True)
        self.FL = wpilib.CANTalon(51)#test these numbers
        self.FR = wpilib.CANTalon(52)
        self.BL = wpilib.CANTalon(53)
        self.BR = wpilib.CANTalon(54)
        self.Lift = wpilib.CANTalon(41)
        self.FR.reverseSensor(flip=-1)
        self.BR.reverseSensor(flip=-1)
        self.Configurer.config(self.FL)
        self.Configurer.config(self.FR)
        self.Configurer.config(self.BL)
        self.Configurer.config(self.BR)
        self.PDP = wpilib.PowerDistributionPanel()
        self.DB = wpilib.SmartDashboard()
        self.StrafeJoystick = wpilib.Joystick(1)
        self.TurnJoystick = wpilib.Joystick(0)
        self.PR = PowerReporter.PowerReporter()
        self.PR.setUp(self.PDP, self.DB)
        self.PR.setDefaultPortNames()
        #USE THESE
        self.Joystick = Joysticks.Joysticks(self.StrafeJoystick, self.TurnJoystick, .1)
        self.MeccanumDrive = Meccanum.Meccanum(self.FL, self.FR, self.BL, self.BR)
        #self.FR.changeControlMode(self, )

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        self.PR.printAll()
        current = self.PDP.getCurrent(0)
        self.MeccanumDrive.update(self.Joystick.getDirection(), self.Joystick.getMagnitude(), self.Joystick.getTurn(), self.Joystick.shouldStartBraking(), self.Joystick.getDriving())
        self.Joystick.updateDrivingState() #updates the WasDriving property to whether you were driving this call
        if (self.StrafeJoystick.getRawButton(3)):
            self.Lift.set(.5)
        elif (self.StrafeJoystick.getRawButton(2)):
            self.Lift.set(-.5)
        else:
            self.Lift.set(0)
        pass

    def testInit(self):
        pass

    def testPeriodic(self):
        pass

    def disabledInit(self):
        pass

if __name__ == "__main__":
    wpilib.run(Buttercraft)