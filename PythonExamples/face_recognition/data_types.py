import sys
from typing import Dict, List, Optional

import face_recognition
import numpy as np
from sortedcontainers import SortedList

from PythonExamples.face_recognition.utils import log

class FaceEncodingStorageItem:
    def __init__(self, encoding: np.ndarray):
        self._encoding_average: np.ndarray = encoding
        self._number_of_items: int = 0

    def update(self, new_encoding: np.ndarray):
        """
        update encoding to keep average data
        @param new_encoding:
        """
        self._encoding_average = (self._encoding_average * self._number_of_items + new_encoding) / (
                self._number_of_items + 1)
        self._number_of_items += 1

    def get_vector(self):
        return self._encoding_average

    def __str__(self):
        return str(self._encoding_average.tolist())

class FaceEncodingStorage:
    def __init__(self, comparison_tolerance: float = 0.6):
        """
        @param comparison_tolerance: when comparing faces, what is considered close enough. smaller is more strict
        """
        self.comparison_tolerance = comparison_tolerance
        self._storage: List[FaceEncodingStorageItem] = []

    def add_update(self, face_encoding: np.ndarray) -> int:
        """
        add or update a face encoding, return existing or new index
        @param tolerance: comparison tolerance, lower values are for more similarities comparisons (0.6 default)
        @param face_encoding:
        """
        best_distance = sys.float_info.max
        best_distance_index = -1
        # look for best distance of known faces encodings
        for i, known_face_encoding in enumerate(self._storage):
            distance = face_recognition.face_distance([known_face_encoding.get_vector()],
                                                      face_encoding)
            log(f'distance: {i} {distance}')
            if distance < best_distance:
                best_distance_index = i
                best_distance = distance
        # if no result found
        if best_distance_index == -1 or best_distance > self.comparison_tolerance:
            self._storage.append(FaceEncodingStorageItem(face_encoding))
            return len(self._storage) - 1
        self._storage[best_distance_index].update(face_encoding)
        return best_distance_index

if __name__ == '__main__':
    array1 = np.array([12.0] * 128, dtype=np.float32)
    array2 = np.array([12.0] * 128, dtype=np.float32)
    array3 = np.array([10.0] * 128, dtype=np.float32)
    item = FaceEncodingStorageItem(array1)
    print(item)
    item.update(array2)
    print(item)
    item.update(array3)
    print(item)
