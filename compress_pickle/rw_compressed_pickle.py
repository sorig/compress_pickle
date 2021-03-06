import gzip
import pickle
import tarfile
import re
import os


def read_gz_pickle(path):
    """ Uncompress and unpickle object from file """
    with gzip.open(path, "rb") as f:
        return pickle.load(f)


def to_gz_pickle(obj, path):
    """ Compress and pickle object to file """
    with gzip.open(path, "wb") as f:
        pickled = pickle.dumps(obj)
        f.write(pickled)


def read_tar_pickle(tar_path, pickle_path):
    """ Extract and unpickle file from tar archive """
    with tarfile.open(tar_path, 'r:gz') as tar:
        f = tar.extractfile(
            pickle_path
        )
        return pickle.load(f)


def read_tar_pickles(tar_path, match_string='.*pickle(\.gz)?'):
    """ Return a list of extracted and unpickled objects with a path in the tar
        file matching the match_string.
    """
    result = []

    with tarfile.open(tar_path, 'r:gz') as tar:
        files = list(filter(
            lambda s: re.match(match_string, s), tar.getnames()
        ))

        for file in files:
            f = tar.extractfile(file)
            result.append(pickle.load(f))

    return result


def list_tar_file_contents(tar_path, filter_match_string='.*pickle(\.gz)?'):
    """ Returns a list of contents of gzipped tar archive """
    with tarfile.open(tar_path, 'r:gz') as tar:
        l = tar.getnames()
        
    return list(filter(lambda s: re.match(filter_match_string, s), l))
