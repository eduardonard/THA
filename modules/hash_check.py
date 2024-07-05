"""
Module for checking the MD5 hash of files.
"""
import hashlib

def md5_hash(file_path):
    """
    Calculate the MD5 hash of the file located at the specified file path.

    Args:
        file_path (str): The path to the file for which to calculate the MD5 hash.

    Returns:
        str: The MD5 hash of the file as a hexadecimal string.
    """

    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
