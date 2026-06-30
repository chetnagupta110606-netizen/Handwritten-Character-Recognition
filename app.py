import streamlit as st
import tensorflow as tf
import numpy as np

from PIL import Image

# ============================
# Load Saved Model
# ============================

model = tf.keras.models.load_model("digit_model.keras")

# ============================
# Streamlit Title
# ============================

st.title("✍️ Handwritten Digit Recognition")

st.write("Upload an image of a handwritten digit.")

# ============================
# Upload Image
# ============================

uploaded_file = st.file_uploader(
    "Choose an Image",
    type=["png", "jpg", "jpeg"]
)

# ============================
# If Image Uploaded
# ============================

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", width=200)

    # Convert to Grayscale
    image = image.convert("L")

    # Resize to 28x28
    image = image.resize((28,28))

    # Convert to NumPy Array
    image = np.array(image)
    image = 255 - image

    # Normalize
    image = image / 255.0

    # Reshape for CNN
    image = image.reshape(1,28,28,1)

    # Prediction
    prediction = model.predict(image)

    digit = np.argmax(prediction)

    st.success(f"Predicted Digit : {digit}")
