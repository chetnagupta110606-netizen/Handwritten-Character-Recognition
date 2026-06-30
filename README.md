# Handwritten Digit Recognition using CNN

## 📌 Project Overview

This project is a Handwritten Digit Recognition System developed using **Convolutional Neural Networks (CNN)** with **TensorFlow/Keras** and **Streamlit**. The model is trained on the **MNIST dataset** to recognize handwritten digits (0–9) from uploaded images.

---

## 🚀 Features

- Recognizes handwritten digits (0–9)
- Uses a Convolutional Neural Network (CNN)
- Trained on the MNIST dataset
- Simple and interactive Streamlit web interface
- Upload an image and get the predicted digit instantly

---

## 🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- Streamlit
- NumPy
- Pillow (PIL)
- OpenCV

---

## 📂 Project Structure

```
Handwritten-Digit-Recognition/
│
├── train.py              # Model training script
├── app.py                # Streamlit application
├── digit_model.keras     # Trained CNN model
├── requirements.txt      # Required Python libraries
├── README.md             # Project documentation
```

---

## 📊 Dataset

The project uses the **MNIST Handwritten Digit Dataset**.

- 60,000 Training Images
- 10,000 Testing Images
- Image Size: 28 × 28 pixels
- Classes: 10 (Digits 0–9)

---

## 🧠 CNN Architecture

The model consists of the following layers:

- Conv2D
- MaxPooling2D
- Flatten
- Dense (128 neurons)
- Dense (10 output neurons with Softmax)

---


## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📷 How to Use

1. Launch the Streamlit application.
2. Upload an image containing a handwritten digit.
3. The trained CNN model processes the image.
4. The predicted digit is displayed on the screen.

---

## 📈 Model Performance

- Test Accuracy: **98.69%**
- Loss Function: Sparse Categorical Crossentropy
- Optimizer: Adam

---

## 📌 Future Improvements

- Support handwritten letters using the EMNIST dataset.
- Recognize multiple digits in a single image.
- Improve preprocessing for real-world handwritten images.
- Deploy the application online using Streamlit Community Cloud.

---

## 🎥 Project Demo

Watch the live demonstration here: https://github.com/chetnagupta110606-netizen/Handwritten-Character-Recognition/blob/main/codeAlpha2.mp4


## 👨‍💻 Author

**Chetna Gupta**

Machine Learning Enthusiast

GitHub: https://github.com/chetnagupta110606-netizen

LinkedIn: https://linkedin.com/in/chetna-gupta-524b86384

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!
