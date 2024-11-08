from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='signalPackage',
            executable='generator_node'
        ),
        Node(
            package='signalPackage',
            executable='modifier_node'
        ),
        Node(
            package='signalPackage',
            executable='viewer_node'
        )
    ])