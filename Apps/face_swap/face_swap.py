import datetime
import shutil

import numpy as np
import os
import os.path as osp
import glob
import cv2
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image

assert insightface.__version__ >= '0.7'

class FaceSwap:
    @staticmethod
    def do_swap(source_img: str = 't1', source_face_index: int = 0, target_img: str = 'tar.jpg',
                result_img: str = 'res.jpg'):
        anaconda_path = r'C:\anaconda3\Lib\site-packages\insightface\data\images'
        shutil.copy(source_img, anaconda_path)
        shutil.copy(target_img, anaconda_path)
        source_img_name = source_img.split('.')[0]
        target_img_name = target_img.split('.')[0]
        app = FaceAnalysis(name='buffalo_l')
        app.prepare(ctx_id=0, det_size=(640, 640))
        swapper = insightface.model_zoo.get_model('inswapper_128.onnx', download=True, download_zip=True)
        src_img = ins_get_image(source_img_name)
        src_faces = app.get(src_img)
        src_faces = sorted(src_faces, key=lambda x: x.bbox[0])
        source_face = src_faces[source_face_index]
        tar_img = ins_get_image(target_img_name)
        tar_faces = app.get(tar_img)
        tar_faces = sorted(tar_faces, key=lambda x: x.bbox[0])
        res_image = tar_img.copy()
        for face in tar_faces:
            res_image = swapper.get(res_image, face, source_face, paste_back=True)
        cv2.imwrite(f"./{result_img}", res_image)
        os.remove(os.path.join(anaconda_path, source_img))
        os.remove(os.path.join(anaconda_path, target_img))
        # res_image = []
        # for face in src_faces:
        #     _img, _ = swapper.get(src_img, face, source_face, paste_back=False)
        #     res_image.append(_img)
        # res_image = np.concatenate(res_image, axis=1)
        # cv2.imwrite("./t1_swapped2.jpg", res_image)

if __name__ == '__main__':
    FaceSwap.do_swap(source_img='1.jpg', source_face_index=0, target_img='2.jpg', result_img='res.jpg')

    def sample():
        app = FaceAnalysis(name='buffalo_l')
        app.prepare(ctx_id=0, det_size=(640, 640))
        swapper = insightface.model_zoo.get_model('inswapper_128.onnx', download=True, download_zip=True)
        shutil.copy('t1.jpg', r'C:\anaconda3\Lib\site-packages\insightface\data\images')
        img = ins_get_image('t1')
        faces = app.get(img)
        faces = sorted(faces, key=lambda x: x.bbox[0])
        assert len(faces) == 6
        source_face = faces[2]
        res = img.copy()
        for face in faces:
            res = swapper.get(res, face, source_face, paste_back=True)
        cv2.imwrite("./t1_swapped.jpg", res)
        res = []
        for face in faces:
            _img, _ = swapper.get(img, face, source_face, paste_back=False)
            res.append(_img)
        res = np.concatenate(res, axis=1)
        cv2.imwrite("./t1_swapped2.jpg", res)

    # sample()
