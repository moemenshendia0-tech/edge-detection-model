import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("Edge Detection Demo 🔍")

st.write("Upload an image and see edge detection result")

# رفع الصورة
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # قراءة الصورة
    image = Image.open(uploaded_file)
    image = np.array(image)

    st.subheader("Original Image")
    st.image(image, channels="RGB")

    # تحويل لـ grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Edge detection (Canny)
    edges = cv2.Canny(gray, 100, 200)

    st.subheader("Edge Detection Result")
    st.image(edges, channels="GRAY")
