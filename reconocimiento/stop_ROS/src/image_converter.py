#!/usr/bin/env python
from __future__ import print_function
import roslib
roslib.load_manifest('prueba')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

min_size      = (10, 10)
image_scale   = 2
haar_scale    = 1.2
min_neighbors = 2
haar_flags    = 0

stop_cascade = cv2.CascadeClassifier('/home/felipe/catkin_ws/src/prueba/haar/stop_cascade.xml')
#hay que cambiar la ruta 

class image_converter:


  def __init__(self):
    self.image_pub = rospy.Publisher("usb_cam/image_processed",Image, queue_size=10)
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("usb_cam/image_raw",Image,self.callback)
    self.object_pub = rospy.Publisher('chatter', String, queue_size=10)
	
    

  def callback(self,data):
    try:
      img = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)
	
    #pub = rospy.Publisher('chatter', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    
    # allocate temporary images
    new_size = (int(img.shape[1] / image_scale), int(img.shape[0] / image_scale))

    # convert color input image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # scale input image for faster processing
    small_img = cv2.resize(gray, new_size, interpolation = cv2.INTER_LINEAR)

    small_img = cv2.equalizeHist(small_img)

    if(stop_cascade):
            stop = stop_cascade.detectMultiScale(small_img, haar_scale, min_neighbors, haar_flags, min_size)
            if stop is not None:
                for (x, y, w, h) in stop:
                    # the input to detectMultiScale was resized, so scale the
                    # bounding box of each face and convert it to two CvPoints
                    pt1 = (int(x * image_scale), int(y * image_scale))
                    pt2 = (int((x + w) * image_scale), int((y + h) * image_scale))
                    cv2.rectangle(img, pt1, pt2, (255, 0, 0), 3, 8, 0)
                    string = "stop"
                    # rospy.loginfo(string)
                    self.object_pub.publish(string)
                    rate.sleep()

    


    cv2.imshow("result", img)
    cv2.waitKey(3)

    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(img, "bgr8"))
      #self.object_pub.publish(string)
    except CvBridgeError as e:
      print(e)

def main(args):
  

  rospy.init_node('image_converter', anonymous=True)
  ic = image_converter()
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
