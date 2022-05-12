#!/usr/bin/env python3

import os
import rospy
from localize_sound.srv import RequestAngle

angle = 0

def get_angle(request):
  if request:
    with open('../../../odas/bin/op.txt') as f:
      lines = f.readlines()
      return int(lines[-3][7:-1])
  else:
    return 400
if __name__ == "__main__":
  rospy.init_node("request_angle_server")
  s = rospy.Service("request_angle", RequestAngle, get_angle)
  print("Angle Request ready")
  rospy.spin()
  
  

