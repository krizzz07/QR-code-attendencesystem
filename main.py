import numpy as np
import cv2
import json
from pyzbar import pyzbar

# Function to load user data from the JSON file
def load_user_data(filename):
    try:
        with open(filename, "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = []
    return data

# Load existing user data from the "data.json" file
user_data = load_user_data("data.json")

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img = cap.read()
    for barcode in pyzbar.decode(img):
        scanned_data = barcode.data.decode('utf-8')
        
        # Check if the scanned ID exists in user data
        user_found = False
        for user in user_data:
            if user['id'] == scanned_data:
                print(user['name'], "logged in")
                output = "Authentication Success"
                mycolor = (0, 255, 0)
                user_found = True
                break

        if not user_found:
            print("Authentication failed")
            output = "Authentication failed"
            mycolor = (0, 0, 255)

        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape(-1, 1, 2)
        cv2.polylines(img, [pts], True, mycolor, 5)
        pts2 = barcode.rect
        cv2.putText(img, output, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, mycolor, 2)

    cv2.imshow("Result", img)
    cv2.waitKey(1)

# Release the camera before exiting
cap.release()
