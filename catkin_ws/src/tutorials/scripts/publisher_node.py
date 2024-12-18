#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def publisher():
    pub = rospy.Publisher('talking_topic', String, queue_size=10)
    rospy.init_node('publisher_node', anonymous=True)
    rate = rospy.Rate(1)  # 1 Hz
    while not rospy.is_shutdown():
        msg = "Hello Samir - %s"% rospy.get_time()
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
