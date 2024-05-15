import bz2


def compress_audio(filename):
    return bz2.compress(filename, compresslevel=9)
