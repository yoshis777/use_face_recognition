import os
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
            File.move_file(os.path.join(os.environ['UNIDENTIFIED_FOLDER']),
                           filename,
                           'cannot find faces in')
    return encoded_files


class Recognizer:
    def __init__(self):
        pass

    def compare(self):
        known_filenames = File.get_filenames(os.path.join(os.environ['KNOWN_FOLDER'], os.environ['TARGET_EXT']))
        unknown_filenames = File.get_filenames(os.path.join(os.environ['UNKNOWN_FOLDER'], os.environ['TARGET_EXT']))[
                            :int(os.environ['PROCESSING_NUM'])]
        print(known_filenames)
        print(unknown_filenames)

        known_faces = encode_files(known_filenames)

        def encode_file(filename):
            try:
                return face_recognition.face_encodings(face_recognition.load_image_file(filename))[0]
            except IndexError:
                File.move_file(os.path.join(os.environ['UNIDENTIFIED_FOLDER']),
                               filename,
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
                    recognized_name = File.extract_filename(known_filenames[min_index])
                    File.move_file(unknown_filenames[index],
                                   os.path.join(os.environ['SORTING_FOLDER'],
                                                Util.delete_filename_num(recognized_name)),
                                   'ok ' + recognized_name + ' ')
