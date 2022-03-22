#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from robot_vision_msgs.msg import BoundingBoxes


def callback_image(msg):
    global frame
    frame = CvBridge().imgmsg_to_cv2(msg, "bgr8")


def callback_boxes(msg):
    global boxes
    boxes = msg.bounding_boxes


if __name__ == "__main__":
    rospy.init_node("demo")
    rospy.loginfo("start!")

    frame = None
    rospy.Subscriber("/camera/rgb/image_raw", Image, callback_image)
    boxes = []
    rospy.Subscriber("/yolo_ros/bounding_boxes", BoundingBoxes, callback_boxes)

    while not rospy.is_shutdown():
        if frame is not None:
            rospy.loginfo("%d" % (len(boxes)))
            for box in boxes:
                rospy.loginfo(box.Class)
            cv2.imshow("frame", frame)
            cv2.waitKey(1)
