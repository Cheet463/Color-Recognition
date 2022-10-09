import csv
import time
from datetime import datetime
import cv2
import numpy as np

# lower boundary RED color range values; Hue (0 - 10)
LOWER1 = np.array([0, 100, 20])
UPPER1 = np.array([10, 255, 255])

# upper boundary RED color range values; Hue (160 - 180)
LOWER2 = np.array([160, 100, 20])
UPPER2 = np.array([179, 255, 255])

pixel_count = 0

fieldnames = ["Date", "Count"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    # Captures video from file
    cap = cv2.VideoCapture('IMG_1968.MOV')

    while(1):
        # Take each frame
        _, frame = cap.read()

        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Setting mask using boundaries
        lower_mask = cv2.inRange(hsv, LOWER1, UPPER1)
        upper_mask = cv2.inRange(hsv, LOWER2, UPPER2)

        # Threshold the HSV image to get only red colors
        full_mask = lower_mask + upper_mask

        # Bitwise-AND mask and original image
        result = cv2.bitwise_and(frame, frame, mask=full_mask)

        cv2.imshow('frame', frame)
        cv2.imshow('mask', full_mask)
        cv2.imshow('result', result)

        # counting the number of pixels
        number_of_white_pix = np.sum(result == 255)
        #number_of_black_pix = np.sum(result == 0)

        with open('data.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            info = {
                "Date": datetime.now(),
                "Count": number_of_white_pix
            }

            csv_writer.writerow(info)
            print(datetime.now(), number_of_white_pix)
        time.sleep(1)