import streamlit as st
from PIL import Image
import os

from script import pipeline 

st.title("Image Segmentation App")

image_name = st.text_input("Enter the image name (e.g., 040.jpg):")

if st.button("Process"):
    input_path = f'images/{image_name}'
    if not os.path.exists(input_path):
        st.error(f"Image file '{image_name}' not found in the 'images/' folder.")
    else:
        st.subheader("Original Image")
        original_image = Image.open(input_path)
        st.image(original_image, caption="Original Image", use_column_width=True)

        with st.spinner("Processing..."):
            try:
                pipeline(image_name)

                output_folder = f'segmented/{image_name}/'
                if not os.path.exists(output_folder):
                    st.error("No segmented images found.")
                else:
                    st.success("Image processed successfully!")

                    st.subheader("Segmented Images")
                    segmented_images = [
                        os.path.join(output_folder, img)
                        for img in os.listdir(output_folder)
                        if img.endswith((".png", ".jpg", ".jpeg"))
                    ]
                    for seg_img in segmented_images:
                        st.image(seg_img, caption=os.path.basename(seg_img), use_column_width=True)
            except Exception as e:
                st.error(f"An error occurred: {e}")
