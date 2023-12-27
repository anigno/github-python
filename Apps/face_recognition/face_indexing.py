import face_recognition
import cv2
import os

from numpy import ndarray

from Apps.face_recognition.data_types import FaceEncodingStorage
from utils import log

class FaceIndexing:
    def __init__(self, results_folder: str = 'results', comparison_tolerance=0.6):
        self.video_captured = None
        self.results_folder = results_folder
        self.storage = FaceEncodingStorage(comparison_tolerance)
        if not os.path.exists(self.results_folder):
            os.mkdir(self.results_folder)

    def index_video_folder(self, videos_folder_path: str, skip_frames: int):
        log(f'starting indexing videos from folder: {videos_folder_path}')
        video_files = os.listdir(videos_folder_path)
        for video_file in video_files:
            video_file = os.path.join(videos_folder_path, video_file)
            if os.path.isfile(video_file):
                self.index_video_file(video_file, skip_frames)

    def index_images_folder(self, images_folder_path: str):
        raise NotImplemented()

    def index_video_file(self, video_file_path: str, skip_frames: int):
        log(f'starting indexing video file: {video_file_path} skip: {skip_frames} frames')
        self.video_captured = cv2.VideoCapture(video_file_path)
        frame_cnt = -1
        while True:
            frame_cnt += 1
            ret, frame = self.video_captured.read()
            if not ret:
                break  # no more frames
            if frame_cnt % skip_frames != 0:
                continue  # skip this frame
            log(f'recognizing: {video_file_path} frame {frame_cnt}')
            # recognize frame
            face_locations = face_recognition.face_locations(frame, 1, 'hog')
            for face_location in face_locations:
                face_encoding_list = face_recognition.face_encodings(frame, [face_location],
                                                                     1, 'small')
                face_encoding_to_process = face_encoding_list[0]
                face_index = self.storage.add_update(face_encoding_to_process)
                self.save_face_image(frame, face_location, face_index)

        self.video_captured.release()

    def save_face_image(self, frame: ndarray, face_location: tuple, face_index: int):
        top, right, bottom, left = face_location
        face = frame[top:bottom, left:right]
        file_dir = os.path.join(self.results_folder, str(face_index))
        if not os.path.exists(file_dir):
            os.mkdir(file_dir)
        num_files = len(os.listdir(file_dir))
        file_path = os.path.join(file_dir, str(num_files) + '.jpg')
        cv2.imwrite(file_path, face)
        log(f'saved face image to index :{face_index}')

if __name__ == '__main__':
    fi = FaceIndexing('D:\\Downloads\\results', 0.5)
    fi.index_video_folder('D:\\Downloads\\sample_videos', 30)
