
import rospy

from std_msgs.msg import String
from geometry_msgs.msg import Twist

p = rospy.Publisher('/turtlebot_2/cmd_vel', Twist)

rospy.init_node('lincoln_publisher')

while not rospy.is_shutdown ():
    t = Twist()
    t.linear.x = 0.3
    t.angular.z = 1.0
    print t
    p.publish(t)
    rospy.sleep(1)
