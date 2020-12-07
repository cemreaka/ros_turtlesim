#! /usr/bin/env python

#18070006007

import rospy
import sys
from geometry_msgs.msg import Twist
import math


rospy.init_node('turtle', anonymous=True)
velocity_publisher = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
vel_msg= Twist()
distance = 1.0
speed = 0.6
vel_msg.linear.x = 0.0
vel_msg.linear.y = 0.0
vel_msg.linear.z = 0.0
vel_msg.angular.x = 0.0
vel_msg.angular.y = 0.0
vel_msg.angular.z = 0.0
        

def turtleMove():    
    rospy.loginfo("Move Turtle!")
    rospy.loginfo(distance)
    vel_msg.linear.x = speed
    t0 = rospy.Time.now().to_sec()    
    current_distance = 0
    while(current_distance < distance):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_distance = speed * (t1-t0)

    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg) 


def turtleTurn(turnspeed, angle, clockwise):
    rospy.loginfo("Rotate Turtle!")
    angular_speed = (turnspeed * math.pi) /180
    relative_angle = (angle * math.pi) / 180
    vel_msg.angular.z = abs(angular_speed) * clockwise

    t0 = rospy.Time.now().to_sec()    
    current_angle = 0

    while(current_angle < relative_angle):
       velocity_publisher.publish(vel_msg)
       t1 = rospy.Time.now().to_sec()
       current_angle = angular_speed * (t1-t0) 

    vel_msg.angular.z = 0 
    velocity_publisher.publish(vel_msg)


def changeDistance(count):
    global distance
    distance += count      

if __name__ =='__main__':
    try:
        for c in range(0,4):
            for t in range(0,2):          
                turtleMove()
                turtleTurn(9, 90, 1) 
            changeDistance(1)  
        rospy.loginfo("Turtle stopped moving")            
    except rospy.ROSInterruptException: pass    


