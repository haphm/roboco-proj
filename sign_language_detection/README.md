Here's a `README.md` file tailored for the [`sign_language_detection`](https://github.com/haphm/roboco-proj/tree/master/sign_language_detection) directory of the RoboCO project:

---

# Sign Language Detection Module – RoboCO Project

This module provides a Python-based implementation for detecting and recognizing sign language gestures using computer vision techniques. It includes tools for collecting gesture images, training a classifier, and performing real-time inference.

## 📁 Contents

- **`collect_images.py`** – Script to capture images of hand gestures for dataset creation.
- **`create_dataset.py`** – Processes collected images and prepares them for training.
- **`train_classifier.py`** – Trains a machine learning model to recognize sign language gestures.
- **`inference_classifier.py`** – Performs real-time gesture recognition using the trained model.
- **`data.pickle`** – Serialized dataset used for training.
- **`model.p`** – Serialized trained model for inference.

## 🛠️ Requirements

- Python 3.6 or higher
- OpenCV (`opencv-python`)
- NumPy
- scikit-learn

Install the dependencies using pip:

```bash
pip install opencv-python numpy scikit-learn
```

## 🚀 Usage

### 1. Collect Gesture Images

To collect images for a specific gesture:

```bash
python collect_images.py
```


Follow the on-screen instructions to capture images of the desired hand gesture.

### 2. Create Dataset

After collecting images, process them to create a dataset:

```bash
python create_dataset.py
```


This will generate a `data.pickle` file containing the processed dataset.

### 3. Train Classifier

Train the model using the created dataset:

```bash
python train_classifier.py
```


This will produce a `model.p` file containing the trained model.

### 4. Real-Time Inference

Use the trained model to perform real-time gesture recognition:

```bash
python inference_classifier.py
```


The script will access your webcam and display the recognized gestures in real-time.

## 🧠 How It Works

The system captures images of hand gestures and processes them to extract relevant features. These features are then used to train a machine learning classifier capable of recognizing different sign language gestures. Once trained, the model can perform real-time inference on live video feed from a webcam.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

---

*Note: This module is part of the larger [RoboCO Project](https://github.com/haphm/roboco-proj), which includes additional components like face recognition and QR code scanning.*

--- 
