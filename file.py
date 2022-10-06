import glob
import os
import pathlib
import shutil


class File:
    def __init__(self):
        pass

    @classmethod
    def get_filenames(cls, target_path):
        return glob.glob(target_path)

    @classmethod
    def extract_filename(cls, filepath):
        return os.path.splitext(os.path.basename(filepath))[0]

    @classmethod
    def move_file(cls, target_filepath, dest_path, message):
        os.makedirs(dest_path, exist_ok=True)
        shutil.move(target_filepath, dest_path)
        print(message + ': ' + target_filepath)

    @classmethod
    def count_files(cls, target_dir_path):
        p_temp = pathlib.Path(target_dir_path)

        return len(list(p_temp.glob('**/' + os.environ['TARGET_EXT'])))

    @classmethod
    def count_files_in_dest_folder(cls):
        dest_dir_files_count = cls.count_files(os.environ['SORTING_FOLDER']) +\
            cls.count_files(os.environ['UNIDENTIFIED_FOLDER']) +\
            cls.count_files(os.environ['THRESHOLD_FOLDER'])

        return dest_dir_files_count
