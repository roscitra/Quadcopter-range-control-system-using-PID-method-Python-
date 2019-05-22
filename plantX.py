#!/usr/bin/env python 

#import library ros 
import rospy
import PID
import time
from numpy import inf
import xlwt



#import library untuk mengirim command dan menerima data navigasi dari quadcopter
from ReadData import uav
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty 


class Position():
    def __init__(self):
        rospy.init_node('Position', anonymous=False)
        self.rate = rospy.Rate(10)        
        self.pubTakeoff = rospy.Publisher("ardrone/takeoff",Empty, queue_size=10)
        self.pubLand = rospy.Publisher("ardrone/land",Empty, queue_size=10)
        self.pubCommand = rospy.Publisher('cmd_vel',Twist, queue_size=10)
        self.command = Twist() 
        self.state_change_time = rospy.Time.now()    
        rospy.on_shutdown(self.SendLand)

    def SendTakeOff(self):
        self.pubTakeoff.publish(Empty()) 
        self.rate.sleep()
                
    def SendLand(self):
        self.pubLand.publish(Empty()) 
    
    def SetCommand(self, linear_x, linear_y, linear_z, angular_x, angular_y, angular_z):
        self.command.linear.x = linear_x
        self.command.linear.y = linear_y
        self.command.linear.z = linear_z
        self.command.angular.x = angular_x
        self.command.angular.y = angular_y
        self.command.angular.z = angular_z
        self.pubCommand.publish(self.command)
        self.rate.sleep()
        
    def posisi(self):
        #variable pid        
        P= 0.042
        I= 0.046
        D= 0.025
        pid = PID.PID(P, I, D)
        pid.SetPoint=0.0 #setpoint sistem = posisi dalam meter
        pid.setSampleTime(0.025)
        pid.last_error=0.0
        
        feedback = 0.0 #feedback sistem
        
        #list
        self.feedback_list = []
        self.time_list = []
        self.setpoint_list = []
        kecepatan=[]
        waktu=[]
        waktu2=[]
        pidawal=[]
        nilaiP=[]        
        nilaiI=[]
        nilaiD=[]
        de=[]

        
        totalX=0.0
        i=0       
        end_time=0.0
        totaltime=0.0
        
        #input range ==================================================
        pid.SetPoint = 10 #you can input negative number to move in the opposite direction
        #===============================================================
        while pid.SetPoint is not None:
            pid.update(feedback)
            self.output = pid.output
            outputawal=self.output
            if self.output > 1:
                self.output = 1
            elif self.output < -1:
                self.output = -1
            print (self.output)
            
            #sending command to ar drone
            start_time = time.clock()
            bless.SetCommand(self.output,0,0,0,0,0)
            
            end_time = time.clock()
            
            #perhitungan jarak tempuh
            timer = end_time - start_time
            totaltime = totaltime + timer
            
            posisiX = uav.vx * timer
            totalX += posisiX 
            
            #feedback
            feedback = totalX
            i+=1

            #list data variabel            
            kecepatan.append(str(uav.vx))
            waktu.append(str(totaltime))
            waktu2.append(str(timer))
            pidawal.append(str(outputawal))
            self.feedback_list.append(feedback)
            self.setpoint_list.append(pid.SetPoint)
            self.time_list.append(i)
            nilaiP.append(pid.PTerm)
            nilaiI.append(pid.ITerm)
            nilaiD.append(pid.DTerm)
            de.append(pid.delta_time)
            #print di terminal
            print ("set point= "+str(pid.SetPoint)) 
            print("-------------------------------------")
            print ("posisi= "+str(totalX))
            print("-------------------------------------")
            print ("kecepatan= "+str(uav.vx))
            print ("start time= "+str(start_time))
            print ("end time= "+str(end_time))
            print ("timer= "+str(timer))
            print("-------------------------------------")
            print ("PID= "+str(outputawal))            
            print ("SetCommand= "+str(self.output))
            print ("last error= "+str(pid.last_error))
            print (i)
            print("=====================================")
            
    
            #export to xls
            wb = xlwt.Workbook()
            ws = wb.add_sheet("data")
            for i, row in enumerate(self.setpoint_list):
                ws.write(i, 0, row)
            for i, row2 in enumerate(self.feedback_list):
                ws.write(i, 1, row2)            
            for i, row3 in enumerate(kecepatan):
                ws.write(i, 2, row3)
            for i, row4 in enumerate(waktu):
                ws.write(i, 3, row4)
            for i, row5 in enumerate(waktu2):
                ws.write(i, 4, row5)
            for i, row6 in enumerate(self.time_list):
                ws.write(i, 5, row6)
            for i, row7 in enumerate(pidawal):
                ws.write(i, 6, row7)
            for i, row8 in enumerate(nilaiP):
                ws.write(i, 7,row8)
            for i, row9 in enumerate(nilaiI):
                ws.write(i, 8,row9)
            for i, row10 in enumerate(nilaiD):
                ws.write(i, 9,row10)
            for i, row11 in enumerate(de):
                ws.write(i, 10,row11)
            wb.save("dataX.xls")
            
            


bless=Position()            
            
if __name__ == '__main__': 
    try:        
        while not rospy.is_shutdown():
                        
            bless.posisi()

    except rospy.ROSInterruptException:
        pass

#timesampling harus sama deengan waktu per loop atau lebih besar sedikit
