import os
import sys

sourceFolder = sys.argv[1]
files = os.listdir(sourceFolder)
for file in files:
    if os.path.isdir(os.path.join(sourceFolder, file)):
        continue
    file_extension_split = file.split('.')
    file_only = file_extension_split[0]
    extension = file_extension_split[1]
    parts = file_only.split('-')
    new_file = ''
    if len(parts) == 1:
        new_file = parts[0]
    if len(parts) == 2:
        new_file = parts[1] + '-' + parts[0]
    if len(parts) == 3:
        new_file = parts[1] + '-' + parts[0]
    new_file = new_file + '.' + extension
    file = os.path.join(sourceFolder, file)
    new_file = os.path.join(sourceFolder, new_file)
    print('------------------------------')
    print(f'{file} -> {new_file}')
    os.rename(src=file, dst=new_file)
