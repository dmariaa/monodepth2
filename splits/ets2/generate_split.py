import random
import glob
import os
import sys


def split(file):
    fsplit = os.path.split(file)
    dsplit = os.path.split(fsplit[0])
    file = fsplit[1]
    dir = dsplit[-1]
    return dir + ' ' + str(int(file[8:-5])) + ' l\n'

train = sys.argv[1] if len(sys.argv) > 1 else 0.95

# lines = open("files.txt", 'r').readlines()
lines = glob.glob("../../train/**/*.bmp")
num_files = len(lines)
val_files = int(num_files * (1-train))

print('train files: ' + str(num_files - val_files))
print('validation files: ' + str(val_files))

# lines = list(map(lambda s: '20210521-000001 ' + str(int(s[8:-5])) + ' l\n', lines[1:-2]))
lines = list(map(split, lines[1: -2]))
random.shuffle(lines)
open("train_files.txt", 'w').writelines(lines[:-val_files])
open("val_files.txt", 'w').writelines(lines[-val_files:])