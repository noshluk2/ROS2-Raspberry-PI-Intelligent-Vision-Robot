import rclpy
from tflite_runtime.interpreter import Interpreter
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os
import numpy as np
from ament_index_python.packages import get_package_share_directory
from pathlib import Path
class camera_sub(Node):

    def __init__(self):
        super().__init__('surveillance_node')
        self.camera_sub = self.create_subscription(Image,'/rpi_video_feed',self.camera_cb,10)

        self.bridge=CvBridge()
        self.package_share_dir = get_package_share_directory("vision_rpi_bot")
        self.model_file = os.path.join(self.package_share_dir, "data","lite-model_ssd_mobilenet_v1_100_320_uint8_nms_1.tflite")
        self.label_file = os.path.join(self.package_share_dir, "data","labels.txt")

    def camera_cb(self, data):
        frame = self.bridge.imgmsg_to_cv2(data,'mono8')
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
        input_image = frame
        input_image = cv2.resize(input_image,(320,320))
        input_image = input_image.reshape(1 , input_image.shape[0],input_image.shape[1],input_image.shape[2])
        input_image = input_image.astype(np.uint8)


        interpreter = Interpreter(model_path=self.model_file)
        interpreter.allocate_tensors()

        # Get input and output tensors.
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()

        input_data = np.array(input_image, dtype=np.uint8)
        interpreter.set_tensor(input_details[0]['index'], input_data)

        text_file = open(self.label_file,"r")
        label_array = text_file.readlines()

        interpreter.invoke()
        predicted_labels = interpreter.get_tensor(output_details[1]['index'])
        predicted_scores = interpreter.get_tensor(output_details[2]['index'])
        top_score = predicted_scores[0][0]
        top_label = label_array[int(predicted_labels[0][0]) ]
        print("Model Output Lables \n",predicted_labels)
        print("Model Output Scores \n",predicted_scores)
        print("-"*10)
        print("Label -> " , top_label )
        print("-"*10)
        if( top_score > 0.71):
            cv2.imwrite(os.path.join(os.path.expanduser('~'),"extracted_images",top_label+str(top_score)+ ".jpg"),frame)
        cv2.imshow('Frame',frame)
        cv2.waitKey(1)



def main(args=None):
    rclpy.init(args=args)

    sensor_sub = camera_sub()

    rclpy.spin(sensor_sub)
    sensor_sub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()