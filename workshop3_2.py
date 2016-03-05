#!/usr/bin/env python

import rospy
import cv2
import numpy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class image_converter:

    def __init__(self):

        cv2.namedWindow("Image window", 1)
        cv2.namedWindow("Image window 2", 1)
        cv2.namedWindow("Image window 3", 1)
        cv2.startWindowThread()
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/turtlebot_2/camera/rgb/image_raw",
                                          Image, self.callback)
        #self.image_sub = rospy.Subscriber("/turtlebot_1/camera/rgb/image_raw",
        #                                  Image, self.callback)

    def callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError, e:
            print e

        bgr_thresh = cv2.inRange(cv_image,
                                 numpy.array([0, 100, 0]),
                                 numpy.array([50, 255, 50]))

        lower = numpy.array([0, 100, 0], dtype = "uint8")
        upper = numpy.array([50, 255, 50], dtype = "uint8")
        
        mask = cv2.inRange(cv_image, lower, upper)
        output = cv2.bitwise_and(cv_image, cv_image, mask = mask)
        

        cv2.imshow("Image window", cv_image)
        cv2.imshow("Image window 2", bgr_thresh)
        cv2.imshow("Image window 3", output)

image_converter()
rospy.init_node('image_converter', anonymous=True)
rospy.spin()
cv2.destroyAllWindows()