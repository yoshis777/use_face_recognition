import os
import re
import shutil

import face_recognition

from file import File


def encode_files(filenames):
    encoded_files = []
    for filename in filenames:
        try:
            encoded_files.append(face_recognition.face_encodings(face_recognition.load_image_file(filename))[0])
        except IndexError:
            print('except encoding: ' + filename)
    return encoded_files


def get_min_index(target_list):
    min_value = min(target_list)
    if min_value >= float(os.environ['THRESHOLD']):
        return None
    return list(target_list).index(min_value)


def delete_filename_num(filename):
    m = re.search(r'(?P<FILENAME>.*)\(\d+\)', filename)
    if m is None:
        return filename
    else:
        return m.group('FILENAME').rstrip()


class Recognizer:
    def __init__(self):
        pass

    def compare(self):
        known_filenames = File.get_filenames(os.path.join(os.environ['KNOWN_FOLDER'], os.environ['TARGET_EXT']))
        unknown_filenames = File.get_filenames(os.path.join(os.environ['UNKNOWN_FOLDER'], os.environ['TARGET_EXT']))[:30]
        print(known_filenames)
        print(unknown_filenames)

        known_faces = encode_files(known_filenames)

        def encode_file(filename):
            try:
                return face_recognition.face_encodings(face_recognition.load_image_file(filename))[0]
            except IndexError:
                target_path = os.path.join(os.environ['UNIDENTIFIED_FOLDER'])
                os.makedirs(target_path, exist_ok=True)
                shutil.move(filename, target_path)
                print('cannot find face in: ' + filename)
                return None
        unknown_faces = list(map(encode_file, unknown_filenames))

        for index, face in enumerate(unknown_faces):
            if face is not None:
                results = face_recognition.face_distance(known_faces, face)
                min_index = get_min_index(results)
                if min_index is not None:
                    print('ok: ' + unknown_filenames[index])
                    recognized_name = File.extract_filename(known_filenames[min_index])
                    target_path = os.path.join(os.environ['SORTING_FOLDER'], delete_filename_num(recognized_name))
                    os.makedirs(target_path, exist_ok=True)
                    shutil.move(unknown_filenames[index], target_path)
                else:
                    print('out of threshold: ' + unknown_filenames[index])
                    target_path = os.path.join(os.environ['THRESHOLD_FOLDER'])
                    os.makedirs(target_path, exist_ok=True)
                    shutil.move(unknown_filenames[index], target_path)
