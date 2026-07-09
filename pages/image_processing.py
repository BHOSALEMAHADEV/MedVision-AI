import os
import cv2
import streamlit as st

from src.image_processing import (
    read_image,
    resize_image,
    convert_rgb,
    grayscale,
    gaussian_blur,
    median_blur,
    bilateral,
    histogram_equalization,
    clahe,
    sharpen,
    edge,
    threshold,
    adaptive,
    otsu,
    save_image
)

# ==========================================================
# PAGE TITLE
# ==========================================================

st.title("Medical Image Processing")

st.write("Upload a medical image and apply preprocessing techniques.")

st.divider()

# ==========================================================
# FILE UPLOAD
# ==========================================================

uploaded_file = st.file_uploader(
    "Choose Medical Image",
    type=["jpg", "jpeg", "png", "bmp", "tif", "tiff"]
)

if uploaded_file:

    os.makedirs("uploads/processed", exist_ok=True)

    image_path = os.path.join(
        "uploads/processed",
        uploaded_file.name
    )

    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    image = read_image(image_path)

    image = resize_image(image)

    rgb = convert_rgb(image)

    st.subheader("Original Image")

    st.image(
        rgb,
        use_container_width=True
    )

    st.divider()

    operation = st.selectbox(
        "Select Processing Method",
        [
            "Grayscale",
            "Gaussian Blur",
            "Median Blur",
            "Bilateral Filter",
            "Histogram Equalization",
            "CLAHE",
            "Sharpen",
            "Edge Detection",
            "Threshold",
            "Adaptive Threshold",
            "OTSU Threshold"
        ]
    )

    processed = None

    if operation == "Grayscale":
        processed = grayscale(image)

    elif operation == "Gaussian Blur":
        processed = gaussian_blur(image)

    elif operation == "Median Blur":
        processed = median_blur(image)

    elif operation == "Bilateral Filter":
        processed = bilateral(image)

    elif operation == "Histogram Equalization":
        processed = histogram_equalization(image)

    elif operation == "CLAHE":
        processed = clahe(image)

    elif operation == "Sharpen":
        processed = sharpen(image)

    elif operation == "Edge Detection":
        processed = edge(image)

    elif operation == "Threshold":
        processed = threshold(image)

    elif operation == "Adaptive Threshold":
        processed = adaptive(image)

    elif operation == "OTSU Threshold":
        processed = otsu(image)

    st.subheader("Processed Image")

    if len(processed.shape) == 2:
        st.image(
            processed,
            channels="GRAY",
            use_container_width=True
        )
    else:
        st.image(
            cv2.cvtColor(processed, cv2.COLOR_BGR2RGB),
            use_container_width=True
        )

    st.divider()

    if st.button("Save Processed Image"):

        save_path = os.path.join(
            "uploads",
            "processed",
            f"processed_{uploaded_file.name}"
        )

        save_image(
            save_path,
            processed
        )

        st.success("Processed image saved successfully.")

        with open(save_path, "rb") as file:

            st.download_button(
                label="Download Processed Image",
                data=file,
                file_name=f"processed_{uploaded_file.name}",
                mime="image/png"
            )