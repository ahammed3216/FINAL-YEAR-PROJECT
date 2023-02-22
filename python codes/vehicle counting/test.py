import cv2
import glob
from vehicle_detector import VehicleDetector

# Load Veichle Detector
vd = VehicleDetector()

# Load images from a folder
image = glob.glob("images/t1.jpg")

vehicles_folder_count = 0

# Loop through all the images


img = cv2.imread("images/t2.jpeg")

vehicle_boxes = vd.detect_vehicles(img)
vehicle_count = len(vehicle_boxes)

# Update total count
vehicles_folder_count += vehicle_count

for box in vehicle_boxes:
    x, y, w, h = box

    cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

    cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)

cv2.imshow("Cars", img)
cv2.waitKey(0)

print("Total current count", vehicles_folder_count)