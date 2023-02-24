import cv2
import glob
import numpy as np
import serial
import time


img=cv2.imread('image.png')

arduino = serial.Serial('COM4', 9600)

defaut_timer=30


side =0
class VehicleDetector:

    def __init__(self):
        # Load Network
        net = cv2.dnn.readNet("python codes/vehicle counting/dnn_model/yolov4.weights", "python codes/vehicle counting/dnn_model/yolov4.cfg")
        self.model = cv2.dnn_DetectionModel(net)
        self.model.setInputParams(size=(832, 832), scale=1 / 255)


        # Allow classes containing Vehicles only
        self.classes_allowed = [2, 3, 5, 6, 7]


    def detect_vehicles(self, img):
        # Detect Objects
        vehicles_boxes = []
        class_ids, scores, boxes = self.model.detect(img, nmsThreshold=0.4)
        for class_id, score, box in zip(class_ids, scores, boxes):
            if score < 0.5:
                # Skip detection with low confidence
                continue

            if class_id in self.classes_allowed:
                vehicles_boxes.append(box)

        return vehicles_boxes


def capture():
    vid=cv2.VideoCapture(0)
    i=0
    while(i<100):

        ret,image=vid.read()

        cv2.imshow('image',image)
        

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        cv2.imwrite('image.png',image)
        i=i+1
    vid.release()
    cv2.destroyAllWindows()



def count(img):

    # Load Veichle Detector
    vd = VehicleDetector()

    vehicles_folder_count = 0

    # Loop through all the images
    vehicle_boxes = vd.detect_vehicles(img)
    vehicle_count = len(vehicle_boxes)

    # Update total count
    vehicles_folder_count += vehicle_count
    print("Total current count", vehicles_folder_count)
    return vehicles_folder_count



def commn(count):
    value=str(count)
    arduino.write(value.encode())





while True:
    cars=0
    timer=0
    for idx in range(1,5):
        
        time.sleep(timer)
        capture()
        img=cv2.imread('image.png')
        cars=count(img)
        if cars==0:
            timer=5
        else:
            timer=cars*5
        commn(timer)
        print("cars on the {} side is {} and the time needed is {}".format(idx,cars,timer))
        cars=0