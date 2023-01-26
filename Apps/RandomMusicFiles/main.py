import random
import sys
import os
import shutil

from os import listdir
from os.path import isfile, join


def getOnlyFiles(path):
    only_files = [f for f in listdir(path) if isfile(join(path, f))]
    return only_files


MAX_FOLDER_SIZE = 699000000

print(f'{len(sys.argv)} {sys.argv}')
sourceFolder = sys.argv[1]

files = getOnlyFiles(sourceFolder)
files = [os.path.join(sourceFolder, file) for file in files]

random.shuffle(files)

cnt = 0
randomFiles = []
for file in files:
    randomFiles.append(file)
    cnt += 1

folderCnt = 0
sizeCnt = 0
fileIndex = 1
for file in randomFiles:
    fileSize = os.path.getsize(file)
    sizeCnt += fileSize
    if sizeCnt >= MAX_FOLDER_SIZE:
        sizeCnt = fileSize
        folderCnt += 1
        fileIndex = 1
    path, filename = os.path.split(file)
    newPath = os.path.join(path, str(folderCnt))
    if not os.path.exists(newPath):
        os.mkdir(newPath)
    newFile = os.path.join(newPath, str(fileIndex).zfill(3) + " " + filename)
    fileIndex += 1
    shutil.copyfile(file, newFile)
