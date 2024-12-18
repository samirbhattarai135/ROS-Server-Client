#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from tutorials.msg import Position


def callback(data):
    rospy.loginfo("%s X: %f Y: %f", data.message, data.x, data.y)

def subscriber():
    rospy.init_node("Subscriber_Node", anonymous=True)
    rospy.Subscriber('talking_topic', Position, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass
