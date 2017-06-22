import os
from pprint import pprint

from file_hasher import get_hash
def duplicate_fider(topdir=None):
    if topdir is None:
        topdir = os.getcwd()    # current working directory

    # rozmiar pliku: lista plików o tym rozmiarze
    data = {}
    hashed_files = set()
    # hash: lista plików o tym samym hashu
    hashes = {}

    for root, dirs, files in os.walk(topdir):

        #print(root, dirs, files, '\n\n')
        for single_file in files:
            f_path = os.path.join(root, single_file)
            size = os.path.getsize(f_path)
            size_list = data.get(size, [])
            size_list.append(f_path)
            data[size] = size_list

            #TODO: policzyć hashe plików z listy

            if len(size_list) > 1:  # sprawdzanie czy lista jest wieksza niż 1
                for file_path in size_list:
                    if file_path not in hashed_files:
                        f_hash = get_hash(file_path)
                        hash_list = hashes.get(f_hash, [])
                        hash_list.append(file_path)
                        hashes[f_hash] = hash_list
                        hashed_files.add(file_path)

    return data, hashes #, hashed_files


pprint(duplicate_fider())

data, hashes = duplicate_fider('/Users/negativeone/Documents/programowanie/Python/daftcode/')



# duplicate_fider('/Users/negativeone/Documents/programowanie/Python/daftcode/')


