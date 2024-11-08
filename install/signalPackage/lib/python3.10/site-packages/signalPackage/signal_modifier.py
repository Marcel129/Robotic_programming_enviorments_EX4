#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class SignalModifier(Node):
    def __init__(self):
        super().__init__("signal_modifier")
        self.msg = Float64()
        self.msg.data = 0.0

        self.signalSubscriber = self.create_subscription(Float64, "/signal", self.signal_callback, 10)

        self.signalPublisher = self.create_publisher(Float64, "/modified_signal", 10)

        self.get_logger().info("Hearing for a signal")

    def signal_callback(self, msg: Float64):
        self.get_logger().info(f"Msg received: {msg.data}")
        self.msg.data = msg.data * 2.0
        self.send_signal_value()

    def send_signal_value(self):
        self.signalPublisher.publish(self.msg)

def main(args=None):
    rclpy.init(args=args)
    node = SignalModifier()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    