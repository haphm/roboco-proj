Here's a `README.md` file tailored for the [`face_reg_code`](https://github.com/haphm/roboco-proj/tree/master/face_reg_code) directory of the RoboCO project:

---

# Face Recognition Module – RoboCO Project

This module provides a Python-based implementation of real-time face recognition using OpenCV. It includes tools for face detection, recognition, and image comparison, suitable for educational and prototyping purposes.

## 📁 Contents

- **`face_streaming.py`** – Captures video from a webcam and performs real-time face recognition.
- **`image_comparison.py`** – Compares two images to determine facial similarity.
- **`simple_facerec.py`** – A utility class that encapsulates face detection and recognition logic.

## 🛠️ Requirements

- Python 3.6 or higher
- OpenCV (`opencv-python`)
- NumPy
- Face Recognition

Install the dependencies using pip:

```bash
pip install opencv-python numpy face-recognition
```


## 🚀 Usage

### 1. Real-Time Face Recognition

To start the webcam-based face recognition:

```bash
python face_streaming.py
```


This script will open your webcam and attempt to recognize faces in real-time.

### 2. Image Comparison

To compare two images for facial similarity:

```bash
python image_comparison.py path_to_image1.jpg path_to_image2.jpg
```


Replace `path_to_image1.jpg` and `path_to_image2.jpg` with the paths to your images.

## 🧠 How It Works

The `simple_facerec.py` script utilizes OpenCV's Haar cascades for face detection and computes facial embeddings for recognition. It serves as a foundational example for understanding face recognition workflows.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

---

*Note: This module is part of the larger [RoboCO Project](https://github.com/haphm/roboco-proj), which includes additional components like QR code scanning and sign language detection.* 
