import os
import pathlib
import re

from dotenv import load_dotenv

from file import File
from recognizer import Recognizer


def main():
    load_dotenv()

    Recognizer().compare()

    # dir = ''
    # dir2 = ''
    #
    # p_temp = pathlib.Path(dir)
    # p_temp2 = pathlib.Path(dir2)
    # print(len(list(p_temp.glob('**/*.jpg'))) - len(list(p_temp2.glob('**/*.jpg'))))


main()
