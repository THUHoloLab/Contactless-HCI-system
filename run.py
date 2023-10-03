# -*- coding: utf-8 -*-
#  -*-coding:utf8 -*-
#--------------------------------------------------------------------#
#                                                                    #
# Copyright (C) 2020 HOLOEYE Photonics AG. All rights reserved.      #
# Contact: https://holoeye.com/contact/                              #
#                                                                    #
# This file is part of HOLOEYE SLM Display SDK.                      #
#                                                                    #
# You may use this file under the terms and conditions of the        #
# "HOLOEYE SLM Display SDK Standard License v1.0" license agreement. #
#                                                                    #
#--------------------------------------------------------------------#

import csv
import sys
import imp
import time
imp.reload(sys)
sys.setdefaultencoding('gbk') 
from pickle import NONE
sys.path.insert(0, "leap motion")
import Leap
import time
import warnings
warnings.filterwarnings('ignore')
from ctypes import sizeof
import math
import cv2
# Import the SLM Display SDK
import detect_heds_module_path
from holoeye import slmdisplaysdk
# Initializes the SLM library
slm = slmdisplaysdk.SLMInstance()
# Check if the library implements the required version
if not slm.requiresVersion(3):
    exit(1)
# Detect SLMs and open a window on the selected SLM
error = slm.open()
assert error == slmdisplaysdk.ErrorCode.NoError, slm.errorString(error)
# Open the SLM preview window in non-scaled mode:
from showSLMPreview import showSLMPreview
# Show preview window
# showSLMPreview(slm, scale=1.0)  

m,n=2160,3840   # Resolution of SLM
# Read the pictures and convert them into grayscale images
def load_reverse_pic(hologram):
    hologram=hologram.astype(float)
    hologram=hologram*2*math.pi/255
    for i in range(m/2):
        for j in range(n):
            var=hologram[i,j]
            hologram[i,j]=hologram[m-1-i,j]
            hologram[m-1-i,j]=var
    return hologram
# You may need to change the path when reading holograms
hologram_0 = cv2.imread("D:\yyx\code\键盘全息图v3_1\hologram\hologram_0_(d=3mm).bmp",0)
hologram_0=load_reverse_pic(hologram_0)
hologram_1 = cv2.imread("D:\yyx\code\键盘全息图v3_1\hologram\hologram_1_(d=3mm).bmp",0)
hologram_1=load_reverse_pic(hologram_1)
hologram_2 = cv2.imread("D:\yyx\code\键盘全息图v3_1\hologram\hologram_2_(d=3mm).bmp",0)
hologram_2=load_reverse_pic(hologram_2)
hologram_3 = cv2.imread("D:\yyx\code\键盘全息图v3_1\hologram\hologram_3_(d=3mm).bmp",0)
hologram_3=load_reverse_pic(hologram_3)
hologram_4 = cv2.imread("D:\yyx\code\键盘全息图v3_1\hologram\hologram_4_(d=3mm).bmp",0)
hologram_4=load_reverse_pic(hologram_4)
hologram_5 = cv2.imread("D:\yyx\code\键盘全息图v3_1\hologram\hologram_5_(d=3mm).bmp",0)
hologram_5=load_reverse_pic(hologram_5)
hologram_6 = cv2.imread("D:\yyx\code\键盘全息图v3_1\hologram\hologram_6_(d=3mm).bmp",0)
hologram_6=load_reverse_pic(hologram_6)
hologram_7 = cv2.imread("D:\yyx\code\键盘全息图v3_1\hologram\hologram_7_(d=3mm).bmp",0)
hologram_7=load_reverse_pic(hologram_7)
hologram_8 = cv2.imread("D:\yyx\code\键盘全息图v3_1\hologram\hologram_8_(d=3mm).bmp",0)
hologram_8=load_reverse_pic(hologram_8)
hologram_9 = cv2.imread("D:\yyx\code\键盘全息图v3_1\hologram\hologram_9_(d=3mm).bmp",0)
hologram_9=load_reverse_pic(hologram_9)
hologram_Del = cv2.imread("D:\yyx\code\键盘全息图v3_1\hologram\hologram_del_(d=3mm).bmp",0)
hologram_Del=load_reverse_pic(hologram_Del)
hologram_dot = cv2.imread("D:\yyx\code\键盘全息图v3_1\hologram\hologram_0_(d=3mm).bmp",0)#
hologram_dot=load_reverse_pic(hologram_dot)
hologram_Enter = cv2.imread("D:\yyx\code\键盘全息图v3_1\hologram\hologram_enter_(d=3mm).bmp",0)
hologram_Enter=load_reverse_pic(hologram_Enter)
hologram_bg=cv2.imread("D:\yyx\code\键盘全息图v3_1\hologram\hologram_0_(d=3mm).bmp",0)#
hologram_bg=load_reverse_pic(hologram_bg)
# Data record formate
header=['x','y','z','frame id','time step','finger']
t0=0.5  #Update interval(second)
# Set the interaction coordinate
z_kb_h0=0   # The position of the Layer-1 in z-direction
z_kb_h1=20 
z_kb_h2=10  
delta_z=15  # Interacting depth of the keyboard in z-direction
global z_flag 
z_flag=0    # A flag of whether the interaction is successful
a=10        # The length and width of a single square button 
y0=170      # The central position of keyboard in y-direction(hight)
# Set the central position of each button in x-y plane
button0_1=[-a*3/2,-a*3/2+y0]
button0_2=[-a/2,-a*3/2+y0]
buttondot=[a/2,-a*3/2+y0]
buttonE1=[a*3/2,-a*3/2+y0]
button1=[-a*3/2,-a/2+y0]
button2=[-a/2,-a/2+y0]
button3=[a/2,-a/2+y0]
buttonE2=[a*3/2,-a/2+y0]
button4=[-a*3/2,a/2+y0]
button5=[-a/2,a/2+y0]
button6=[a/2,a/2+y0]
buttonD1=[a*3/2,a/2+y0]
button7=[-a*3/2,a*3/2+y0]
button8=[-a/2,a*3/2+y0]
button9=[a/2,a*3/2+y0]
buttonD2=[a*3/2,a*3/2+y0]
interact_button=''  # A Record for the interacting button

class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']        
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']   
    def on_init(self, controller):
        print ("Initialized")
    def on_connect(self, controller):
        print ("Connected")
    def on_disconnect(self, controller):
        print ("Disconnected")
    def on_exit(self, controller):
        print ("Exited")
    def on_frame(self, controller):
        global ws
        def search(zmin_finger,button): # Determine the conditions for interaction
            if (zmin_finger[0]>button[0]-a/2) & (zmin_finger[0]<=button[0]+a/2):
                if (zmin_finger[1]>button[1]-a/2) & (zmin_finger[1]<=button[1]+a/2):
                    return button
                else:
                    return [0,0]
            else:
                return [0,0]
        frame = controller.frame()
        # Initialize the data
        row=[0,0,0,0,0,0]                  
        zmin_finger=[0,0,0,0,0,0]          
        data=[0,0,0]
        myhand=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]] 
        # Get hands
        for hand in frame.hands:
            slm.showPhasevalues(hologram_bg)
            print("initialize")
            handType = "Left hand" if hand.is_left else "Right hand"
            normal = hand.palm_normal
            direction = hand.direction
            # Get arm bone
            arm = hand.arm       
            # Get fingers
            for finger in hand.fingers:
                # Get bones
                for b in range(0, 4):
                    bone = finger.bone(b)
                    row=[0,0,0,0,0,0]
                    if(b==3):   
                        row[0],row[1],row[2]= bone.prev_joint[0],bone.prev_joint[1],bone.prev_joint[2]
                        row[3]=frame.id
                        row[4]=frame.timestamp
                        row[5]=str(finger)
                        finger_flag=row[5][-1]  
                        print(row)
                        if(finger_flag=='0'):
                            myhand[0]=row
                        if(finger_flag=='1'):
                            myhand[1]=row
                            data[0],data[1],data[2]=row[0],row[1],row[2]
                        if(finger_flag=='2'):
                            myhand[2]=row
                        if(finger_flag=='3'):
                            myhand[3]=row
                        if(finger_flag=='4'):
                            myhand[4]=row
            zmin_finger=myhand[0]
            for j in range(1,5):
                if myhand[j][2]<=zmin_finger[2]:
                    zmin_finger=myhand[j]                                
            global z_flag
            z_flag=0    
            if (zmin_finger[2]>=z_kb_h1-delta_z) & (zmin_finger[2]<=z_kb_h2+delta_z):
                z_flag=1    
            global interact_button
            interact_button='' 
            T1=time.time()
            # Search the interacting button and upload the corresponding hologram
            if search(zmin_finger,buttonE1)!=[0,0] or search(zmin_finger,buttonE2)!=[0,0]:
                            interact_button='Enter'
                            print("press Enter")
                            slm.showPhasevalues(hologram_Enter)
                            print("show Enter")
                            time.sleep(t0)
                            slm.showPhasevalues(hologram_bg)
                            print("initialize")
            elif search(zmin_finger,buttonD1)!=[0,0] or search(zmin_finger,buttonD2)!=[0,0]:
                            interact_button='Delete'
                            print("press Del")
                            slm.showPhasevalues(hologram_Del)
                            print("show Del")                         
                            time.sleep(t0)
            elif search(zmin_finger,button0_1)!=[0,0] or search(zmin_finger,button0_2)!=[0,0]:
                            interact_button='0'
                            print("press 0")
                            slm.showPhasevalues(hologram_0)
                            print("show 0")
                            time.sleep(t0)
            elif search(zmin_finger,buttondot)!=[0,0]:
                            interact_button='.'
                            print("press dot")
                            slm.showPhasevalues(hologram_dot)
                            print("show dot")                         
                            time.sleep(t0)
            elif search(zmin_finger,button1)!=[0,0]:
                            interact_button='1'
                            print("press 1")  
                            slm.showPhasevalues(hologram_1)
                            print("show 1")                             
                            time.sleep(t0)                    
            elif search(zmin_finger,button2)!=[0,0]:
                            interact_button='2'                
                            print("press 2")
                            slm.showPhasevalues(hologram_2)
                            print("show 2")                            
                            time.sleep(t0)
            elif search(zmin_finger,button3)!=[0,0]:
                            interact_button='3'
                            print("press 3")
                            slm.showPhasevalues(hologram_3)
                            print("show 3")                                
                            time.sleep(t0)                        
            elif search(zmin_finger,button4)!=[0,0]:
                            interact_button='4'
                            print("press 4")
                            slm.showPhasevalues(hologram_4)
                            print("show 4")                             
                            time.sleep(t0)                         
            elif search(zmin_finger,button5)!=[0,0]:
                            interact_button='5'   
                            print("press 5")
                            slm.showPhasevalues(hologram_5)
                            print("show 5")                               
                            time.sleep(t0)                                                
            elif search(zmin_finger,button6)!=[0,0]:
                            interact_button='6'
                            print("press 6")
                            slm.showPhasevalues(hologram_6)
                            print("show 6")                              
                            time.sleep(t0)                      
            elif search(zmin_finger,button7)!=[0,0]:
                            interact_button='7'
                            print("press 7") 
                            slm.showPhasevalues(hologram_7)
                            print("show 7")                              
                            time.sleep(t0)                        
            elif search(zmin_finger,button8)!=[0,0]:
                            interact_button='8'
                            print("press 8")
                            slm.showPhasevalues(hologram_8)
                            print("show 8")                            
                            time.sleep(t0)                        
            elif search(zmin_finger,button9)!=[0,0]:
                            interact_button='9'
                            print("press 9")
                            slm.showPhasevalues(hologram_9)
                            print("show 9")                          
                            time.sleep(t0)
            else:
                            interact_button=''
            T2=time.time()
            if(interact_button!=''):
                data=[interact_button,(T2 - T1)*1000]
                writer.writerows([data])
                print('run time:%sms' % ((T2 - T1)*1000))  

def main():
    showSLMPreview(slm, scale=1.0)      
    slm.showPhasevalues(hologram_bg)
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()
    # Have the sample listener receive events from the controller
    controller.add_listener(listener)
    # Keep this process running until Enter is pressed
    print ("Press Enter to quit...")
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)

if __name__ == "__main__":
    with open ('time.csv','wb') as fp:
        writer =csv.writer(fp)
        main()
    

