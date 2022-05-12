#!/usr/bin/env python
import rospy
from zed_interfaces.msg import ObjectsStamped, Skeleton2D, Keypoint2Df

def callback(data):
    teack_obj_id = []
    for object_ in data.objects:
        if object_.skeleton_available:
            # rospy.loginfo(object_.skeleton_2d.keypoints[0].kp[1])
            if (object_.skeleton_2d.keypoints[7].kp[1] < object_.skeleton_2d.keypoints[6].kp[1]) or \
                 (object_.skeleton_2d.keypoints[4].kp[1] < object_.skeleton_2d.keypoints[3].kp[1]):
                rospy.loginfo("Hand Raise Detected " + object_.label + str(object_.label_id))
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('hand_raise_recog', anonymous=True)

    rospy.Subscriber("/zed2i/zed_node/obj_det/objects", ObjectsStamped, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
