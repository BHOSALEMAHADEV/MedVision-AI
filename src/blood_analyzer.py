import cv2
import numpy as np


def analyze_blood(image_path):

    image = cv2.imread(image_path)

    original = image.copy()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (9, 9), 2)

    circles = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=20,
        param1=50,
        param2=25,
        minRadius=8,
        maxRadius=35
    )

    total_cells = 0

    if circles is not None:

        circles = np.round(circles[0]).astype("int")

        total_cells = len(circles)

        for (x, y, r) in circles:

            cv2.circle(original, (x, y), r, (0,255,0), 2)

            cv2.circle(original, (x, y), 2, (0,0,255), 3)

    return original, total_cells