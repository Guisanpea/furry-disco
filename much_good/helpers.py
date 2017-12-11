from os import listdir

from os.path import isfile, join
from random import randint


def compute_gcd(a, b):
    return a if b == 0 else compute_gcd(b, a % b)


def random_file_name(path):
    files = [file for file in listdir(path) if isfile(join(path, file))]
    return join(path, files[randint(0, len(files)-1)])
