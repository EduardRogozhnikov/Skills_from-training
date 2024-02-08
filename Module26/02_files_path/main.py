# TODO здесь писать код
import os


def gen_files():
    folder = os.path.abspath(os.path.join('..'))

    for links, dirs, files in list(os.walk(folder)):
        for file in files:
            print(links + '\\' + file)


gen_files()
