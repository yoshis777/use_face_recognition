import os
import re


class Util:
    def __init__(self):
        pass

    @classmethod
    def get_min_index(cls, target_list):
        min_value = min(target_list)
        if min_value >= float(os.environ['THRESHOLD']):
            return None
        return list(target_list).index(min_value)

    @classmethod
    def delete_filename_num(cls, filename):
        m = re.search(r'(?P<FILENAME>.*)\(\d+\)', filename)
        if m is None:
            return filename
        else:
            return m.group('FILENAME').rstrip()

