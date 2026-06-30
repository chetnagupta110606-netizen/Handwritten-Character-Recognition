import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# ===========================
# Load MNIST Dataset
# ===========================

(X_train, y_train), (X_test, y_test) = mnist.load_data()

print("Training Images :", X_train.shape)
print("Testing Images :", X_test.shape)

# ===========================
# Normalize Images
# ===========================

X_train = X_train / 255.0
X_test = X_test / 255.0

# ===========================
# Add Channel Dimension
# ===========================

X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)

# ===========================
# Build CNN Model
# ===========================

model = Sequential()

# Convolution Layer
model.add(
    Conv2D(
        filters=32,
        kernel_size=(3,3),
        activation="relu",
        input_shape=(28,28,1)
    )
)

# Pooling Layer
model.add(
    MaxPooling2D(pool_size=(2,2))
)

# Convert 2D to 1D
model.add(
    Flatten()
)

# Hidden Layer
model.add(
    Dense(
        128,
        activation="relu"
    )
)

# Output Layer
model.add(
    Dense(
        10,
        activation="softmax"
    )
)

# ===========================
# Compile Model
# ===========================

model.compile(

    optimizer="adam",

    loss="sparse_categorical_crossentropy",

    metrics=["accuracy"]

)

# ===========================
# Train Model
# ===========================

model.fit(

    X_train,

    y_train,

    epochs=5,

    validation_data=(X_test, y_test)

)

# ===========================
# Test Accuracy
# ===========================

loss, accuracy = model.evaluate(X_test, y_test)

print("Accuracy :", accuracy)

# ===========================
# Save Model
# ===========================

model.save("digit_model.keras")

print("Model Saved Successfully!")

