import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
class video_publisher(Node):

    def __init__(self):
        super().__init__('rpi_video_publisher')
        self.publisher_ = self.create_publisher(Image, '/rpi_video_feed', 10)
        timer_period = 0.05  # seconds
        self.timer = self.create_timer(timer_period, self.camera_callback)
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
        self.bridge = CvBridge()

    def camera_callback(self):
        ret, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = self.bridge.cv2_to_imgmsg(frame,'mono8')
        self.publisher_.publish(frame)


def main(args=None):
    rclpy.init(args=args)

    publisher = video_publisher()
    print("Note Started")
    rclpy.spin(publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()