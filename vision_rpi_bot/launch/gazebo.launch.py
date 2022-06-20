import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    package_share_dir = get_package_share_directory("vision_rpi_bot")
    urdf_file_path = os.path.join(package_share_dir, "urdf","vision_rpi_bot.urdf")
    urdf = open(urdf_file_path).read()


    return LaunchDescription(
        [
            ExecuteProcess(
                cmd=["gazebo","-s","libgazebo_ros_factory.so",],
                output="screen",
            ),

            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                parameters=[{'robot_description': urdf}],
            ),
            Node(
                package="gazebo_ros",
                executable="spawn_entity.py",
                arguments=["-topic","robot_description",
                           "-entity","vision_bot"],#,"-Y","1.57"],
                output= 'screen'
            ),
        ]
    )