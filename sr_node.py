#!/usr/bin/env python
import rospy
import speech_recognition as sr
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("sr")
    rospy.loginfo("Speech Recognition Started.")
    msg=rospy.Publisher("record",String,queue_size=1)

    r = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                rospy.loginfo("Say something!")
                audio = r.listen(source, timeout=5)
            rospy.loginfo("call recognize_goole")
        
            s = r.recognize_google(audio)
            rospy.loginfo(s)
            msg.publish(s)
        except Exception as e:
            rospy.loginfo(e)        
