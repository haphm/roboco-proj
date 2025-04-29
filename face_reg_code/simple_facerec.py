import face_recognition
import cv2
import os
import glob
import numpy as np


class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings = []  # List to store encodings of known faces
        self.known_face_names = []  # List to store names corresponding to known faces

        self.frame_resizing = 0.25  # Resize factor for faster face detection

    def load_encoding_images(self, images_path):
        # Get list of all image file paths in the directory
        images_path = glob.glob(os.path.join(images_path, "*.*"))

        print("{} encoding images found.".format(len(images_path)))

        # Process each image
        for img_path in images_path:
            img = cv2.imread(img_path)  # Read image using OpenCV
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert image to RGB

            # Extract filename (used as label)
            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)

            # Generate face encoding from the image (assumes one face per image)
            img_encoding = face_recognition.face_encodings(rgb_img)[0]

            # Store the encoding and name
            self.known_face_encodings.append(img_encoding)
            self.known_face_names.append(filename)

        print("Encoding images loaded")

    def detect_known_faces(self, frame):
        # Resize frame for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)

        # Convert the image from BGR (OpenCV) to RGB (face_recognition)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Locate faces and get their encodings in the resized frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []  # To store recognized names
        for face_encoding in face_encodings:
            # Compare current face with known faces
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            # Get distances to all known faces
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            # Check if best match is actually a valid match
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]

            face_names.append(name)

        # Scale back face locations to match the original frame size
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing

        return face_locations.astype(int), face_names  # Return locations and names of recognized faces

