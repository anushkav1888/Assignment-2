#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
from an.srv import text, textRequest
class ArUcoMarkerClient:
    def __init__(self):
        self.bridge = CvBridge()
        self.cap=cv2.VideoCapture(0)
        rospy.init_node('client_node')
        request=textRequest()
        while not rospy.is_shutdown():
            ret, frame=self.cap.read()
            if not ret:
                break
            request.imgs=self.bridge.cv2_to_imgmsg(frame,"bgr8")
            response=self.clientfunc(request)
            rospy.loginfo("response received %s" %response)
    def clientfunc(self,request1):
        try :
            rospy.wait_for_service('service')
            try :
                proxy=rospy.ServiceProxy('service',text)
                response=proxy(request1)
                return response
            except rospy.ServiceException as e:
                pass
 
        except rospy.ServiceException as e:
            rospy.loginfo('service call failed %s' %e)
if  __name__ == '__main__':
    ArUcoMarkerClient()

