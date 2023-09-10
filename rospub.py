#!/usr/bin/env python

import rospy
from std_msgs.msg import String  # Import the message type you want to publish

def simple_publisher():
    # Initialize the ROS node with a unique name (you can change "simple_publisher_node")
    rospy.init_node('simple_publisher_node', anonymous=True)

    # Create a publisher that publishes messages of type String on the "my_topic" topic
    pub = rospy.Publisher('my_topic', String, queue_size=10)

    rate = rospy.Rate(1)  # Set the publishing rate to 1 Hz

    while not rospy.is_shutdown():
        message = "Hello, ROS!"  # Create a message
        rospy.loginfo(message)  # Log the message to the console
        pub.publish(message)  # Publish the message on the topic
        rate.sleep()  # Sleep to maintain the publishing rate

if __name__ == '__main__':
    try:
        simple_publisher()
    except rospy.ROSInterruptException:
        pass
