import os
from os.path import exists, join, isfile
from shutil import copy, rmtree


def clean_directory(dir:str):
    if exists(dir):
        rmtree(dir)
    os.mkdir(dir)

def copy_files(source:str, destination:str):
    files = os.listdir(source)
    for file in files:
        path = join(source, file)
        if isfile(path):
            copy(path, destination)
        else:
            new_dir = os.mkdir(join(destination, file))
            copy_files(path, join(destination, file))

def copy_static_files(source:str, destination:str):
    clean_directory(destination)
    copy_files(source, destination)

