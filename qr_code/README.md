Here's a `README.md` file tailored for the [`qr_code`](https://github.com/haphm/roboco-proj/tree/master/qr_code) directory of the RoboCO project:

---

# QR Code Module – RoboCO Project

This module provides Python-based tools for generating and reading QR codes, as well as managing a whitelist of authorized QR codes. It's designed for educational purposes and prototyping within the RoboCO project.

## 📁 Contents

- **`qrcode_generator.py`** – Generates QR codes from input data.
- **`qrcode_reader.py`** – Reads and decodes QR codes from images or a webcam feed.
- **`whitelist.txt`** – A list of authorized QR code data entries.
- **`log.txt`** – Logs of scanned QR codes and their validation status.
- **`qr_code_data/`** – Directory containing sample QR code images.

## 🛠️ Requirements

- Python 3.6 or higher
- OpenCV (`opencv-python`)
- NumPy
- qrcode

Install the dependencies using pip:

```bash
pip install opencv-python numpy qrcode
```

## 🚀 Usage

### 1. Generate a QR Code

To generate a QR code from input data:

```bash
python qrcode_generator.py
```


This will create a QR code image saved in the `qr_code_data/` directory.

### 2. Read and Validate a QR Code

To read and validate a QR code from an image:

```bash
python qrcode_reader.py
```


The script will open your webcam and attempt to recognize QR code in real-time, decode the QR code and check if the data is present in `whitelist.txt`. The result will be logged in `log.txt`.

## 🧠 How It Works

- **QR Code Generation**: The `qrcode_generator.py` script uses the `qrcode` library to create QR codes from input strings.
- **QR Code Reading**: The `qrcode_reader.py` script utilizes OpenCV to detect and decode QR codes from streaming video. It then compares the decoded data against entries in `whitelist.txt` to determine authorization.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

---

*Note: This module is part of the larger [RoboCO Project](https://github.com/haphm/roboco-proj), which includes additional components like face recognition and sign language detection.*

--- 
