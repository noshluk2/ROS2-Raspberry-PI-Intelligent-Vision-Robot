import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    os.system("export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp")

    return LaunchDescription(
        [

            Node(
                package="vision_rpi_bot",
                executable="image_publisher",
            ),
            Node(
                package="vision_rpi_bot",
                executable="cmdVel_to_pwm_node",
                output='screen'
            ),

        ]
    )