from typing import List, Tuple

import face_recognition
import cv2
import os
from numpy import ndarray

class CV2Wrapper:
    def video_open(self) -> cv2.VideoCapture:
        video_capture = cv2.VideoCapture(file)
        return video_capture

    def video_read_frame(self, video_capture: cv2.VideoCapture) -> Tuple[bool, ndarray]:
        ret, frame = video_capture.read()
        return ret, frame

    def video_release(self, video_capture: cv2.VideoCapture):
        video_capture.release()

    def image_read(self, image_path: str):
        frame = cv2.imread(image_path)
        return frame

class FaceRecognitionWrapper:
    def read_image(self, image_path: str) -> ndarray:
        frame = face_recognition.load_image_file(image_path)
        return frame

    def calculate_face_in_location_encoding(self, face_frame: ndarray,
                                            face_locations: List[Tuple[int, int, int, int]]) -> List[ndarray]:
        encodings = face_recognition.face_encodings(face_frame, face_locations)
        return encodings

    def calculate_all_faces_encoding(self, face_frame: ndarray) -> List[ndarray]:
        encodings = face_recognition.face_encodings(face_frame)
        return encodings

    def get_faces_locations(self, frame: ndarray, samples=1) -> List[ndarray]:
        faces_locations = face_recognition.face_locations(frame, samples)
        return faces_locations

VIDEOS_PATH = 'D:\\Downloads\\sample_videos'
OUTPUT_PATH = "D:\\Downloads\\extracted_faces"

if not os.path.exists(OUTPUT_PATH):
    os.mkdir(OUTPUT_PATH)

video_files = os.listdir(VIDEOS_PATH)
for file in video_files:
    file = os.path.join(VIDEOS_PATH, file)
    print(f'{file}')
    video = cv2.VideoCapture(file)
    frame_cnt = -1
    while True:
        frame_cnt += 1
        # Read the next frame from the video.
        ret, frame = video.read()
        if frame_cnt % 10 != 0:
            continue
        print(f'frame: {file} {frame_cnt}')

        # If the frame is empty, break the loop.
        if not ret:
            break
        # Detect faces in the frame.
        face_locations = face_recognition.face_locations(frame)
        # If there are any faces in the frame, group them together.
        face_groups = []
        known_encodings_lists: List[List] = []
        for face_location in face_locations:
            face_encodings = face_recognition.face_encodings(frame, face_locations)
            d = face_recognition.face_distance()
            c = face_recognition.compare_faces()
            face_group = []
            for other_face_location in face_locations:
                if face_recognition.compare_faces(np.array([face_location, ]), np.array(other_face_location),
                                                  tolerance=0.05):
                    face_group.append(other_face_location)
            face_groups.append(face_group)

        # Extract the faces from the frame and save them to separate images.
        for face_group in face_groups:
            for face_location in face_group:
                top, right, bottom, left = face_location
                face = frame[top:bottom, left:right]

                # Create a directory for the person if it doesn't exist.
                person_dir = os.path.join(OUTPUT_PATH, str(len(face_groups)))
                if not os.path.exists(person_dir):
                    os.mkdir(person_dir)

                # Save the face to a separate image.
                cv2.imwrite(os.path.join(person_dir, f"face_{len(face_group)}_{frame_cnt}.jpg"), face)
    video.release()
