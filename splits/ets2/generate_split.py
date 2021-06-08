import random
import glob
import os
import sys


def split(file):
    fsplit = os.path.split(file)
    dsplit = os.path.split(fsplit[0])
    file = fsplit[1]
    dir = dsplit[-1]
    file_number = int(file[8:-4])
    if file_number==0:
        print(file + " -> " + str(file_number))
    return dir + ' ' + str(file_number) + ' l\n'

train = sys.argv[1] if len(sys.argv) > 1 else 0.95

dirs = glob.glob("../../train/*/")
files = []

for dir in dirs:
    fname = os.path.join(dir, '*.bmp')
    f = glob.glob(fname)
    f = f[1:-1]
    print("{}: {}".format(fname, len(f)))
    files.extend(f)

num_files = len(files)
val_files = int(num_files * (1-train))

print('train files: ' + str(num_files - val_files))
print('validation files: ' + str(val_files))

lines = list(map(split, files[1: -1]))
random.shuffle(lines)
open("train_files.txt", 'w').writelines(lines[:-val_files])
open("val_files.txt", 'w').writelines(lines[-val_files:])