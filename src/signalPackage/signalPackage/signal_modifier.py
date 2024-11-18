#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class SignalModifier(Node):
    def __init__(self):
        super().__init__("signal_modifier")
        self.declare_parameters(
            namespace='',
            parameters=[
                ('signal_scaling_factor', rclpy.Parameter.Type.DOUBLE)
            ]
        )
        self.msg = Float64()
        self.msg.data = 0.0
        self.scalingFactor = self.get_parameter('signal_scaling_factor').get_parameter_value().double_value

        self.get_logger().info(
            f"""Hearing for a signal has been started
            Loaded params values: 
            scaling factor: {self.scalingFactor}""")
        
        self.signalSubscriber = self.create_subscription(Float64, "/signal", self.signal_callback, 10)

        self.signalPublisher = self.create_publisher(Float64, "/modified_signal", 10)


    def signal_callback(self, msg: Float64):
        self.msg.data = msg.data * self.scalingFactor
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
    