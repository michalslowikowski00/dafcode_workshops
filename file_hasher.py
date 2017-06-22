"""
import hashlib


def get_hash(f_path, mode='md5'):
    h = hashlib.new(mode)
    f = open(f_path, "rb")  # open file
    h.update(f.read())
    hash_text = h.hexdigest()
    f.close()   # close file | file should be always close after using
    return hash_text

# print(get_hash('./Users/negativeone/Documents', 'sha1'))
"""

import hashlib
import logging


CHUNK_SIZE = 8192


def get_hash(f_path, mode='md5'):
    h = hashlib.new(mode)
    try:
        with open(f_path, 'rb') as f:
            while buff:
                h.update(buff)
                buff = f.read(CHUNK.SIZE)
            return h.hexdigest()
    except OSError as e:
        logging.warning(
            "Got an error during file {} opening."
            "Error: {}". format(f_path, e)
        )
