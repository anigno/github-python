import os
import random
import shutil
import time
import cv2
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image

assert insightface.__version__ >= '0.7'

class FaceSwap:
    app = FaceAnalysis(name='buffalo_l')
    swapper = insightface.model_zoo.get_model('inswapper_128.onnx', download=True, download_zip=True)

    anaconda_path = r'C:\anaconda3\Lib\site-packages\insightface\data\images'

    @staticmethod
    def do_swap(source_img: str = 't1', source_face_index: int = 0, target_img: str = 'tar.jpg',
                result_img: str = 'res.jpg'):
        shutil.copy(source_img, FaceSwap.anaconda_path)
        shutil.copy(target_img, FaceSwap.anaconda_path)
        source_img_name = source_img.split('.')[0]
        target_img_name = target_img.split('.')[0]
        FaceSwap.app.prepare(ctx_id=0, det_size=(640, 640))
        src_img = ins_get_image(source_img_name)
        src_faces = FaceSwap.app.get(src_img)
        src_faces = sorted(src_faces, key=lambda x: x.bbox[0])
        if not src_faces:
            return False
        source_face = src_faces[source_face_index]
        tar_img = ins_get_image(target_img_name)
        tar_faces = FaceSwap.app.get(tar_img)
        tar_faces = sorted(tar_faces, key=lambda x: x.bbox[0])
        res_image = tar_img.copy()
        for face in tar_faces:
            res_image = FaceSwap.swapper.get(res_image, face, source_face, paste_back=True)
        cv2.imwrite(f"./{result_img}", res_image)
        return True
        # os.remove(os.path.join(anaconda_path, source_img))
        # os.remove(os.path.join(anaconda_path, target_img))
        # res_image = []
        # for face in src_faces:
        #     _img, _ = swapper.get(src_img, face, source_face, paste_back=False)
        #     res_image.append(_img)
        # res_image = np.concatenate(res_image, axis=1)
        # cv2.imwrite("./t1_swapped2.jpg", res_image)

    @staticmethod
    def swap_multi(main_dir):
        src_dir = os.path.join(main_dir, 'src')
        tar_dir = os.path.join(main_dir, 'tar')
        res_dir = os.path.join(main_dir, 'res')
        tar_list = os.listdir(tar_dir)
        src_list = os.listdir(src_dir)
        total = len(tar_list) * (len(src_list))
        count = 1
        start_time = time.time()
        print(f'\n****** targets={len(tar_list)} sources={len(src_list)} total={total} ******\n')
        for j, tar in enumerate(tar_list):
            for i, src in enumerate(src_list):
                result = FaceSwap.do_swap(os.path.join(src_dir, src), 0, os.path.join(tar_dir, tar), 'res.jpg')
                if result:
                    r = random.randint(100000, 999999)
                    shutil.move('res.jpg', os.path.join(res_dir, f'res_{j}_{i}_{r}.jpg'))
                time_passed = time.time() - start_time
                time_per_swap = time_passed / count
                time_left = time_per_swap * (total - count)
                print(f'\n****** {count}/{total} time left: {int(time_left) // 60}:{int(time_left) % 60}  time per swap: {int(time_per_swap)} sec******\n')
                count += 1
        FaceSwap.del_files(FaceSwap.anaconda_path)

    @staticmethod
    def del_files(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            # Check if the path is a file
            if os.path.isfile(file_path):
                # Delete the file
                os.remove(file_path)

if __name__ == '__main__':
    FaceSwap.swap_multi(r'O:\swap\someone')
    # def sample(),:
    #     app = FaceAnalysis(name='buffalo_l')
    #     app.prepare(ctx_id=0, det_size=(640, 640))
    #     swapper = insightface.model_zoo.get_model('inswapper_128.onnx', download=True, download_zip=True)
    #     shutil.copy('t1.jpg', r'C:\anaconda3\Lib\site-packages\insightface\data\images')
    #     img = ins_get_image('t1')
    #     faces = app.get(img)
    #     faces = sorted(faces, key=lambda x: x.bbox[0])
    #     assert len(faces) == 6
    #     source_face = faces[2]
    #     res = img.copy()
    #     for face in faces:
    #         res = swapper.get(res, face, source_face, paste_back=True)
    #     cv2.imwrite("./t1_swapped.jpg", res)
    #     res = []
    #     for face in faces:
    #         _img, _ = swapper.get(img, face, source_face, paste_back=False)
    #         res.append(_img)
    #     res = np.concatenate(res, axis=1)
    #     cv2.imwrite("./t1_swapped2.jpg", res)

    # sample()
