import csv
import time
from datetime import datetime
import cv2
import numpy as np
import os.path


def start():
    # lower boundary RED color range values; Hue (0 - 10)
    LOWER1 = np.array([0, 100, 20])
    UPPER1 = np.array([10, 255, 255])

    # upper boundary RED color range values; Hue (160 - 180)
    LOWER2 = np.array([160, 100, 20])
    UPPER2 = np.array([179, 255, 255])

    white_pix_count = 0

    HEADERS = ["Date", "Count"]

    FILENAME = 'data.csv'
    file_exists = os.path.isfile(FILENAME)

    with open(FILENAME, 'w') as new_csv_file:
        csv_writer = csv.DictWriter(new_csv_file,
                                    delimiter=',',
                                    lineterminator='\n',
                                    fieldnames=HEADERS)

        if not file_exists:
            csv_writer.writeheader()

    # Captures video from file
    cap = cv2.VideoCapture('IMG_1968.MOV')
    frame_count = 0

    while cap.isOpened():

        # Take each frame
        is_success, frame = cap.read()

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
        white_pix_count += np.sum(result == 255)
        # number_of_black_pix = np.sum(result == 0)
        frame_count += 1
        print(datetime.now(), white_pix_count)
        if frame_count == 10:
            with open(FILENAME, 'a') as csv_file:
                update_writer = csv.DictWriter(csv_file,
                                               delimiter=',',
                                               lineterminator='\n',
                                               fieldnames=HEADERS)

                info = {
                    "Date": datetime.now(),
                    "Count": white_pix_count/10
                }

                update_writer.writerow(info)
                print(f"Average is {white_pix_count/10}")
                time.sleep(1)
                frame_count = 0
                white_pix_count = 0


if __name__ == '__main__':
    start()
