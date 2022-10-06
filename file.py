import glob
import os


class File:
    def __init__(self):
        pass

    @classmethod
    def get_filenames(cls, target_path):
        return glob.glob(target_path)

    @classmethod
    def extract_filename(cls, filepath):
        return os.path.splitext(os.path.basename(filepath))[0]
