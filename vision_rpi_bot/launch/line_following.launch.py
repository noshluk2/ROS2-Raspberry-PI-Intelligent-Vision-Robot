import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    package_share_dir = get_package_share_directory("vision_rpi_bot")
    urdf_file_path = os.path.join(package_share_dir, "urdf","vision_rpi_bot.urdf")
    world_file_path = os.path.join(package_share_dir, "worlds","lineFollow.world")



    return LaunchDescription(
        [
            ExecuteProcess(
                cmd=["gazebo","--verbose",world_file_path,"-s","libgazebo_ros_factory.so",],
                output="screen",
            ),
        ]
    )