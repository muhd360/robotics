#!/usr/bin/env python

import rospy
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton
from std_msgs.msg import String

class ROSGui(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.init_ros()

    def init_ui(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("ROS Subscriber GUI")

        self.textbox = QTextEdit(self)
        self.textbox.setReadOnly(True)
        self.textbox.setGeometry(10, 10, 380, 220)

        self.start_button = QPushButton("Start", self)
        self.start_button.setGeometry(10, 240, 100, 50)
        self.start_button.clicked.connect(self.start_display)

    def init_ros(self):
        rospy.init_node('simple_subscriber_node', anonymous=True)

        # Create a subscriber to listen to a specific topic
        rospy.Subscriber('my_topic', String, self.message_callback)

    def message_callback(self, msg):
        # Display the received message in the textbox
        self.textbox.append(msg.data)

    def start_display(self):
        # Start displaying messages when the "Start" button is clicked
        self.textbox.clear()  # Clear the textbox
        self.textbox.append("Displaying messages...")
        

def main():
    app = QApplication(sys.argv)
    ros_gui = ROSGui()
    ros_gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
