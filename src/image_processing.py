import cv2
import numpy as np


# ==========================================
# Read Image
# ==========================================

def read_image(path):

    image = cv2.imread(path)

    return image


# ==========================================
# Save Image
# ==========================================

def save_image(path, image):

    cv2.imwrite(path, image)


# ==========================================
# Resize
# ==========================================

def resize_image(image, width=512, height=512):

    return cv2.resize(image, (width, height))


# ==========================================
# Convert to RGB
# ==========================================

def convert_rgb(image):

    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# ==========================================
# Convert to Grayscale
# ==========================================

def grayscale(image):

    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# ==========================================
# Gaussian Blur
# ==========================================

def gaussian_blur(image):

    return cv2.GaussianBlur(image, (5,5), 0)


# ==========================================
# Median Blur
# ==========================================

def median_blur(image):

    return cv2.medianBlur(image, 5)


# ==========================================
# Bilateral Filter
# ==========================================

def bilateral(image):

    return cv2.bilateralFilter(image,9,75,75)


# ==========================================
# Histogram Equalization
# ==========================================

def histogram_equalization(image):

    gray = grayscale(image)

    return cv2.equalizeHist(gray)


# ==========================================
# CLAHE
# ==========================================

def clahe(image):

    gray = grayscale(image)

    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8,8)
    )

    return clahe.apply(gray)


# ==========================================
# Sharpen
# ==========================================

def sharpen(image):

    kernel = np.array([
        [0,-1,0],
        [-1,5,-1],
        [0,-1,0]
    ])

    return cv2.filter2D(image,-1,kernel)


# ==========================================
# Canny Edge
# ==========================================

def edge(image):

    gray = grayscale(image)

    return cv2.Canny(gray,100,200)


# ==========================================
# Threshold
# ==========================================

def threshold(image):

    gray = grayscale(image)

    _,th = cv2.threshold(
        gray,
        120,
        255,
        cv2.THRESH_BINARY
    )

    return th


# ==========================================
# Adaptive Threshold
# ==========================================

def adaptive(image):

    gray = grayscale(image)

    return cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )


# ==========================================
# OTSU
# ==========================================

def otsu(image):

    gray = grayscale(image)

    _,th = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY+cv2.THRESH_OTSU
    )

    return th