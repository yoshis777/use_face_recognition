import os
import pprint
import shutil
import face_recognition

from file import File
from util import Util


def encode_files(filenames):
    # エンコード後のファイルが多次元配列で、filter関数でNoneを削除できないため、Noneを格納せず追加する
    encoded_files = []
    for filename in filenames:
        try:
            encoded_files.append(face_recognition.face_encodings(face_recognition.load_image_file(filename))[0])
        except IndexError:
            known_name = File.get_containing_dirname(filename)
            File.move_file(filename,
                           os.path.join(os.environ['KNOWN_UNIDENTIFIED_FOLDER'], known_name),
                           'known but cannot find faces in')
    return encoded_files


class Recognizer:
    def __init__(self):
        pass

    def compare(self):
        known_filenames = File.get_filenames_containing_subdir(os.path.join(os.environ['SORTED_FOLDER']))
        unknown_filenames = File.get_filenames(os.path.join(os.environ['UNKNOWN_FOLDER'], os.environ['TARGET_EXT']))[
                            :int(os.environ['PROCESSING_NUM'])]
        pprint.pprint(unknown_filenames)

        known_faces = encode_files(known_filenames)

        def encode_file(filename):
            try:
                return face_recognition.face_encodings(face_recognition.load_image_file(filename))[0]
            except IndexError:
                File.move_file(filename,
                               os.path.join(os.environ['UNIDENTIFIED_FOLDER']),
                               'cannot find faces in')
                return None
        unknown_faces = list(map(encode_file, unknown_filenames))

        for index, face in enumerate(unknown_faces):
            if face is not None:
                results = face_recognition.face_distance(known_faces, face)
                min_index = Util.get_min_index(results)
                if min_index is None:
                    File.move_file(unknown_filenames[index],
                                   os.path.join(os.path.join(os.environ['THRESHOLD_FOLDER'])),
                                   'out of threshold')
                else:
                    recognized_name = File.get_containing_dirname(known_filenames[min_index])
                    File.move_file(unknown_filenames[index],
                                   os.path.join(os.environ['SORTED_FOLDER'], recognized_name),
                                   'ok ' + recognized_name + ' ')
