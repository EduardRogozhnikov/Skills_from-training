# TODO здесь писать код
import os


class File:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        if not os.path.exists(self.file_name):
            open(self.file_name, 'w').close()
        self.file = open(self.file_name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type and issubclass(exc_type, IOError):
            return True
