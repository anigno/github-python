installation:
0. install cmake
1. install anaconda to c:\anaconda3\
2. create python project with face_swap.py
3. set python interpreter to c:\anaconda3\scripts\conda.exe (c:\anaconda3\python.exe)
3.5 install ms build tools BuildTools_Full 2015.exe (see docs or https://github.com/bycloudai/InstallVSBuildToolsWindows?tab=readme-ov-file)
4. using project terminal install: (C:\anaconda3\Scripts\pip install opencv-python)
    pip install opencv-python
    pip install -U insightface
    pip install -U onnxruntime-gpu
5. copy inswapper_128.onnx to c:\Users\anign\.insightface\models\
6 ensure c:\Users\anign\.insightface\models\buffalo_l\ folder exist with: (it should be downloaded)
    1k3d68.onnx
    2d106det.onnx
    det_10g.onnx
    genderage.onnx
    w600k_r50.onnx
    (if not extract buffalo_l.zip)


