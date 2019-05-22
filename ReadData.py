#!/usr/bin/env python 

from matplotlib import pyplot as plt
#import library ros 
import rospy 


#import library untuk mengirim command dan menerima data navigasi dari quadcopter
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty 
from ardrone_autonomy.msg import Navdata


#import class status untuk menentukan status ddari quadcopter

class NavData():
    def __init__(self):
        #rospy.init_node('ReadData', anonymous=False)
        self.subNavdata = rospy.Subscriber('/ardrone/navdata', Navdata, self.ReceiveNavData)
        """self.imuData = rospy.Subscriber('ardrone/imu',Imu, self.GetImuData)"""
        self.roll = 0
        self.roll_dot = 0
        self.pitch = 0
        self.pitch_dot = 0
        self.yaw = 0
        self.yaw_dot = 0
        self.Z = 0
        self.Z_dot = 0
    
                
        
    def ReceiveNavData(self,navdata):
        self.roll = navdata.rotX
        self.pitch = navdata.rotY
        self.yaw = navdata.rotZ
        self.X = navdata.ax
        self.Y = navdata.ay
        self.Z = navdata.az
        self.altd = navdata.altd
        self.rotorA = navdata.motor1
        self.rotorB = navdata.motor2
        self.rotorC = navdata.motor3
        self.rotorD = navdata.motor4
        self.Z = navdata.altd
        self.Z_dot = navdata.vz
        self.vx = navdata.vx
	self.vy = navdata.vy
        
    """def GetImuData(self,Imu):
        self.roll_dot = Imu.angular_velocity.x
        self.pitch_dot = Imu.angular_velocity.y
        self.yaw_dot = Imu.angular_velocity.z"""
        
     
uav = NavData()
