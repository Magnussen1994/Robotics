#!/usr/bin/env python

import rospy
from cv2 import namedWindow, cvtColor, imshow
from cv2 import destroyAllWindows, startWindowThread
from cv2 import COLOR_BGR2GRAY
from cv2 import blur
from numpy import mean
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from std_msgs.msg import String

class image_converter:

    def __init__(self):

        namedWindow("Image window", 1)
        namedWindow("blur", 1)
        self.bridge = CvBridge()
        startWindowThread()
        self.image_sub = rospy.Subscriber("/turtlebot_1/camera/rgb/image_raw",
                                          Image, self.callback)

    def callback(self, data):
        cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")

        gray_img = cvtColor(cv_image, COLOR_BGR2GRAY)
        img2 = blur(gray_img, (3, 3))
        imshow("blur", img2)
        print mean(img2)

        imshow("Image window", gray_img)
        
        pub = rospy.Publisher('/result_topic', String, queue_size=10)
        pub.publish(mean)

rospy.init_node('image_converter')
ic = image_converter()
rospy.spin()

destroyAllWindows()