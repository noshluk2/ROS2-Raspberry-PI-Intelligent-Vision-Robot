from setuptools import setup
import os
from glob import glob
package_name = 'vision_rpi_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name,'meshes'),glob('meshes/*')),
        (os.path.join('share',package_name,'launch'),glob('launch/*')),
        (os.path.join('share',package_name,'urdf'),glob('urdf/*')),
        (os.path.join('share',package_name,'worlds'),glob('worlds/*')),
        (os.path.join('share',package_name,'data'),glob('data/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='luqman',
    maintainer_email='luqman@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'publisher_node = vision_rpi_bot.publisher:main',
                'subscriber_node = vision_rpi_bot.subscriber:main',
                'qr_maze_solve_node = vision_rpi_bot.qr_maze_drive:main',
                'line_following_sim_node = vision_rpi_bot.line_following_sim:main',
                'line_following_real_node = vision_rpi_bot.line_following_real:main',
                'surveillance_node = vision_rpi_bot.surveillance_bot:main',
                           ],
                },
)
