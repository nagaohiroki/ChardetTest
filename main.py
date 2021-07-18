import chardet
import os
import sys

def enc(path):
    for root, _, files in os.walk(path):
        for file in files:
            path = os.path.join(root, file)
            with open(path, mode='rb') as f:
                print(path, chardet.detect(f.read()))


if __name__ == '__main__':
    enc(sys.argv[1])
