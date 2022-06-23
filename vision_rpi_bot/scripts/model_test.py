from tflite_runtime.interpreter import Interpreter
import numpy as np
import os
import cv2
main_dir_path=os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
model_file = os.path.join(main_dir_path,'data','lite-model_ssd_mobilenet_v1_100_320_uint8_nms_1.tflite')
input_file = os.path.join(main_dir_path,'resource','vehicle.jpg')
label_file = os.path.join(main_dir_path,'resource','labels.txt')

## Loading labels
text_file = open(label_file,"r")
label_array = text_file.readlines()

# Load the TFLite model and allocate tensors.
interpreter = Interpreter(model_path=model_file)
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Testing Model on real data
camera_img = cv2.imread(input_file)
input_image = cv2.resize(camera_img,(320,320))
input_image = input_image.reshape(1 , input_image.shape[0],input_image.shape[1],input_image.shape[2])
input_image = input_image.astype(np.uint8)

input_data = np.array(input_image, dtype=np.uint8)
interpreter.set_tensor(input_details[0]['index'], input_data)

interpreter.invoke() # prediction / inference
output_data = interpreter.get_tensor(output_details[1]['index'])


print("Model Output\n",output_data)
print("-"*10)
print("Label -> " , label_array[int(output_data[0][0]) ] )
