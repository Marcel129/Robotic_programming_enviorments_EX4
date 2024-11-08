from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    src_dir = '/home/marcel/studies/2_sem_mgr/RPE_lab/EX4/ros2_ws/src/signalPackage'
    layout_file = os.path.join(
        src_dir, 
        'config', 
        'signalPackage_plotjugglerLayout.xml'
    )

    return LaunchDescription([
        Node(
            package='signalPackage',
            executable='generator_node',
            parameters=[os.path.join(
                src_dir,
                'config',
                'originalSignal_params.yaml'
            )]
        ),
        Node(
            package='signalPackage',
            executable='modifier_node',
            parameters=[os.path.join(
                src_dir,
                'config',
                'modificationSignal_params.yaml'
            )]
        ),
        Node(
            package='plotjuggler',
            executable='plotjuggler',
            name='plotjuggler',
            arguments=['--plugin', 'ROS2', '--layout', layout_file],
            output='screen'
        )
    ])