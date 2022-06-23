import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import Int16
from cv_bridge import CvBridge
import cv2

class camera_sub(Node):

    def __init__(self):
        super().__init__('line_following_node')
        self.camera_sub = self.create_subscription(Image,'/rpi_video_feed',self.camera_cb,10)
        self.error_value_publisher = self.create_publisher(Int16, '/line_following_error', 10)
        self.error_msg = Int16()

        self.bridge=CvBridge()



    def camera_cb(self, data):
        frame = self.bridge.imgmsg_to_cv2(data,'mono8')
        frame=cv2.resize(frame, (640,480), interpolation = cv2.INTER_AREA)
        roi = frame[307:477,185:595] # First is Y and sencond is X
        # blurred_frame = cv2.GaussianBlur(roi, (7,7), 2)
        edged = cv2.Canny(roi, 90,120)

        white_index=[]
        mid_point_line = 0
        for index,values in enumerate(edged[:][139]): # This is in Y Axis
            if(values == 255):
                white_index.append(index)
        # print(white_index)

        if(len(white_index) == 2 ):
            cv2.circle(img=edged, center = (white_index[0],139), radius = 2 , color = (255,0,0), thickness=2)
            cv2.circle(img=edged, center = (white_index[1],139), radius = 2 , color = (255,0,0), thickness=2)
            mid_point_line = int ( (white_index[0] + white_index[1]) /2 )
            cv2.circle(img=edged, center = (mid_point_line,139), radius = 3 , color = (255,0,0), thickness=3)

        mid_point_robot = [205,139]
        cv2.circle(img=edged, center = (mid_point_robot[0],mid_point_robot[1]), radius = 5 , color = (255,0,0), thickness=4)
        self.error_msg.data = int(mid_point_robot[0] - mid_point_line)
        self.error_value_publisher.publish(self.error_msg)



        cv2.imshow('Frame',frame)
        cv2.imshow('Canny Output',edged)
        cv2.waitKey(1)


def main(args=None):
    rclpy.init(args=args)

    sensor_sub = camera_sub()

    rclpy.spin(sensor_sub)
    sensor_sub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()