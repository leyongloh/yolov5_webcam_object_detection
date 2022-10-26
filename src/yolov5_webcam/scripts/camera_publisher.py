#!/usr/bin/python3
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

bridge = CvBridge()


class Camera_publisher(Node):

    def __init__(self):
        super().__init__('camera_publisher')
        self.publisher_ = self.create_publisher(Image, 'rgb_cam/image_raw', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.camera_callback)
        self.i = 0

    def camera_callback(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error openning camera")
            exit()
        ret, frame = cap.read()
        if not ret:
            print("Error receiving frame")
            exit()
        msg = bridge.cv2_to_imgmsg(frame, "bgr8")
        self.publisher_.publish(msg)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)
    camera_publisher = Camera_publisher()
    rclpy.spin(camera_publisher)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

