#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class SignalViewer(Node):
    def __init__(self):
        super().__init__("signal_viewer")
        self.signalSubscriber = self.create_subscription(Float64, "/signal", self.signal_callback, 10)
        self.modifiedSignalSubscriber = self.create_subscription(Float64, "/modified_signal", self.modified_signal_callback, 10)
        self.get_logger().info("Hearing for a signal")

    def signal_callback(self, msg: Float64):
        self.get_logger().info(f"Sygnal oryginalny: {msg.data}")

    def modified_signal_callback(self, msg: Float64):
        self.get_logger().info(f"Sygnal zmodyfikowany: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = SignalViewer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    