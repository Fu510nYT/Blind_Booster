#!/usr/bin/env python
import rospy
from  std_msgs.msg import String
import pyttsx3

def callback_speak(msg):
    global a
    rospy.loginfo(msg.data)
    a=msg.data

if __name__=="__main__":
    rospy.init_node("demo1")
    a=""
    rospy.Subscriber("/say_something",String,callback_speak)
    rospy.loginfo("node: demo1 started.")
    while not rospy.is_shutdown():
        if a!="":
            rospy.loginfo("say")
            engine=pyttsx3.init()
            engine.say(a)
            rospy.loginfo(a)
            engine.runAndWait()
        a=""
