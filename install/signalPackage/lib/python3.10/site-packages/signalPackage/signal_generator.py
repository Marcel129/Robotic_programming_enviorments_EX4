#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import numpy as np

class SignalGenerator(Node):
    def __init__(self):
        super().__init__("signal_generator")
        self.declare_parameters(
            namespace='',
            parameters=[
                ('signal_amplitude', rclpy.Parameter.Type.DOUBLE ),
                ('signal_period', rclpy.Parameter.Type.DOUBLE)
            ]
        )
        self.signalPublisher = self.create_publisher(Float64, "/signal", 10)
        self.timer = self.create_timer(0.5, self.send_signal_value)

        self.signalAmplitude = self.get_parameter('signal_amplitude').get_parameter_value().double_value
        self.signalPeriod = self.get_parameter('signal_period').get_parameter_value().double_value

        sampling_rate = 100 
        t = np.linspace(0, self.signalPeriod, int(sampling_rate * self.signalPeriod), endpoint=False)
        self.signalValues = self.signalAmplitude * np.sin(2 * np.pi * (1/self.signalPeriod) * t)
        self.currentSample = 0
        self.numberOfSamples = len(self.signalValues)

        self.get_logger().info(
            f"""Signal generating has been started.
            Loaded params values: 
            amplitude: {self.signalAmplitude}
            period: {self.signalPeriod}""")

    def send_signal_value(self):
        msg = Float64()
        msg.data = self.signalValues[self.currentSample]
        self.currentSample = (self.currentSample + 1) % self.numberOfSamples
        self.signalPublisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = SignalGenerator()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    