#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import random as rd

class SignalGenerator(Node):
    def __init__(self):
        super().__init__("signal_generator")
        self.cmd_vel_pub = self.create_publisher(Float64, "/signal", 10)
        self.timer = self.create_timer(0.1, self.send_signal_value)
        self.get_logger().info("Signal generating has been started")

    def send_signal_value(self):
        msg = Float64()
        msg.data = rd.random()
        self.cmd_vel_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = SignalGenerator()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    