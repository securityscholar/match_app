import streamlit as st
import cv2
from PIL import Image
import numpy as np
from skimage.metrics import structural_similarity as ssim

# Streamlit app setup
st.title("Photo Comparison App")
st.write("Upload two photos to compare them. If they match, you'll see a thumbs up. Otherwise, you'll see a thumbs down.")

# File upload inputs
file1 = st.file_uploader("Upload the first photo", type=["jpg", "jpeg", "png"])
file2 = st.file_uploader("Upload the second photo", type=["jpg", "jpeg", "png"])

def compare_images(image1, image2, threshold=0.9):
    # Convert images to grayscale
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    
    # Resize images to the same size for comparison
    gray1 = cv2.resize(gray1, (300, 300))
    gray2 = cv2.resize(gray2, (300, 300))
    
    # Compare images using Structural Similarity Index (SSIM)
    score, _ = ssim(gray1, gray2, full=True)
    
    # Determine if images match based on threshold
    return score >= threshold

if file1 and file2:
    # Load images
    image1 = Image.open(file1)
    image2 = Image.open(file2)
    
    # Convert images to OpenCV format
    image1_cv = cv2.cvtColor(np.array(image1), cv2.COLOR_RGB2BGR)
    image2_cv = cv2.cvtColor(np.array(image2), cv2.COLOR_RGB2BGR)
    
    # Display images side by side
    st.image([image1, image2], caption=["Photo 1", "Photo 2"], width=300)
    
    # Perform comparison
    if compare_images(image1_cv, image2_cv):
        st.success("✅ Photos match!")
    else:
        st.error("❌ Photos do not match!")
