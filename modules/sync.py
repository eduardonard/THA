"""
This module contains the functions to synchronize two folders.
"""
import os
import logging
import shutil
from .hash_check import md5_hash


def create_or_update(source: str, replica: str) -> None:
    """
    Synchronizes the contents of the `source` directory with the `replica` directory.
    
    Args:
        source (str): The path to the source directory.
        replica (str): The path to the replica directory.
    
    Returns:
        None
    """
    for root, _, files in os.walk(source):
        relative_path = os.path.relpath(root, source)
        replica_dir = os.path.join(replica, relative_path)
        if not os.path.exists(replica_dir):
            os.makedirs(replica_dir)
            logging.info("Created directory: %s", replica_dir)

        for file in files:
            source_file = os.path.join(root, file)
            replica_file = os.path.join(replica_dir, file)
            if not os.path.exists(replica_file) or md5_hash(source_file) != md5_hash(replica_file):
                shutil.copy2(source_file, replica_file)
                logging.info("Copied/Updated file: %s to %s", source_file, replica_file)

def delete_files(source: str, replica: str) -> None:
    """
    Deletes files in the `replica` directory that do not exist
     in the corresponding `source` directory.

    Args:
        source (str): The path to the `source` directory.
        replica (str): The path to the `replica` directory.
    
    Returns:
        None
    """
    for root, _, files in os.walk(replica):
        relative_path = os.path.relpath(root, replica)
        source_dir = os.path.join(source, relative_path)
        if not os.path.exists(source_dir):
            shutil.rmtree(root)
            logging.info("Deleted directory: %s", root)
            continue

        for file in files:
            replica_file = os.path.join(root, file)
            source_file = os.path.join(source_dir, file)
            if not os.path.exists(source_file):
                os.remove(replica_file)
                logging.info("Deleted file: %s", replica_file)


def sync_directories(source: str, replica: str) -> None:
    """
    Synchronizes the contents of the `source` directory with the `replica` directory.

    Args:
        source (str): The path to the source directory.
        replica (str): The path to the replica directory.

    Returns:
        None
    """
    if not os.path.exists(replica):
        os.makedirs(replica)
        logging.info("Created directory: %s", replica)
    create_or_update(source, replica)
    delete_files(source, replica)
