import random

lines = open("files.txt", 'r').readlines()
lines = list(map(lambda s: '20210521-000001 ' + str(int(s[8:-5])) + ' l\n', lines[1:-2]))
random.shuffle(lines)
open("train_files.txt", 'w').writelines(lines[:-300])
open("val_files.txt", 'w').writelines(lines[-300:])