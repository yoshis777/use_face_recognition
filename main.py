import os
import pathlib
import re

from dotenv import load_dotenv

from file import File
from recognizer import Recognizer


def main():
    load_dotenv()

    print('移動前ファイル数: ' + str(File.count_files_in_dest_folder()))
    Recognizer().compare()
    print('移動後ファイル数: ' + str(File.count_files_in_dest_folder()))


main()
