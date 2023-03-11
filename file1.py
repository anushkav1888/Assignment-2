#!/usr/bin/env python3
import rospy 
from cv_bridge import CvBridge
import imutils  
import cv2 
import sys
from sensor_msgs.msg import Image 
from std_msgs.msg import Float64MultiArray
from an.srv import text,textResponse 

class Arucom:
    def __init__(self):
        rospy.init_node("my_node")
        self.bridge=CvBridge()
        rospy.Service("service",text,self.serverfunc)
        rospy.spin()
    def serverfunc(self, msg):
        arucoDict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_100)
        arucoParams = cv2.aruco.DetectorParameters()
        detector=cv2.aruco.ArucoDetector(arucoDict,arucoParams)
        img1=self.bridge.imgmsg_to_cv2(msg.imgs,"bgr8")
        img1=imutils.resize(img1, width=1000)
        (corners, ids, rejected) = detector.detectMarkers(img1)
        z=Float64MultiArray()
        y=Float64MultiArray()
        z.data=list(ids)
        y.data=list(corners)
        print(z)
        print(y)
            
        
if  __name__=='__main__':
   Arucom()     