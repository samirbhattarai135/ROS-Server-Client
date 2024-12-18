import rospy
from tutorials.srv import multiplier, multiplierResponse

def callback(request):
    return multiplierResponse(request.a * request.b)

def multiply():
    rospy.init_node("multiplier_service")
    rospy.loginfo("Server service started")
    service = rospy.Service("multiplier", multiplier, callback)
    rospy.spin()
    
if __name__ == '__main__':
    multiply()
