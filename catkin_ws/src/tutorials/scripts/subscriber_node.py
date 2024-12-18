#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


def callback(data):
    rospy.loginfo("Received data: %s", data.data)

def subscriber():
    rospy.init_node("Subscriber_Node", anonymous=True)
    rospy.Subscriber('talking_topic', String, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass
