#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:45:25 2019

@author: spidey
"""

from naoqi import ALProxy
import time
import roslib
import rospy
from kobuki_msgs.msg import SensorState

nao_ip='10.111.14.131'
kobuki_base_max_charge = 160

def get_charge():
    rospy.init_node('kobuki_battery',anonymous=True)
    rospy.Subscriber("/mobile_base/sensors/core",SensorState,sensorPowerEventCallback)
    #rospy.spin()

def sensorPowerEventCallback(battery_message):
    charge=round(float(battery_message.battery) / float(kobuki_base_max_charge) * 100)
    rospy.loginfo("Kobuki's battery is now: " + str(round(float(battery_message.battery) / float(kobuki_base_max_charge) * 100)) + "%")    
    tts=ALProxy('ALTextToSpeech','10.111.14.131',9559)
    tts.setParameter('speed', 75)
    if charge>50:
        tts.say('Hey you should be working harder')
        rospy.loginfo('Finished moving')
    else:
        tts.say('You will be tired soon... finish your work here')
    

if __name__=='__main__':
    try:
        get_charge()
    except rospy.ROSInterruptException:
		rospy.loginfo("exception")
    
