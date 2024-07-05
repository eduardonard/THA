"""
Tests for the `sync` module.
"""
import os
import hashlib
import tempfile
import pytest
from modules.hash_check import md5_hash

# Fixture to create a temporary file with specified content
@pytest.fixture
def create_temp_file():
    def _create_temp_file(content):
        fd, path = tempfile.mkstemp()
        with os.fdopen(fd, 'wb') as tmp:
            tmp.write(content)
        return path

    yield _create_temp_file

# Cleanup - ensure temporary files are deleted
def cleanup(file_path):
    try:
        os.remove(file_path)
    except OSError:
        pass

    yield cleanup

# Test to check md5 hash calculation for a file
def test_calculate_md5(create_temp_file):
    temp_file_path = create_temp_file(b"hello world")
    expected_hash = hashlib.md5(b"hello world").hexdigest()
    assert md5_hash(temp_file_path) == expected_hash

# Test to check if md5 hash of the same file is consistent
def test_md5_same_file(create_temp_file):
    temp_file_path = create_temp_file(b"hello world")
    assert md5_hash(temp_file_path) == md5_hash(temp_file_path)

# Test to check if md5 hash of different files are different
def test_md5_different_file(create_temp_file):
    temp_file_path1 = create_temp_file(b"hello world")
    temp_file_path2 = create_temp_file(b"goodbye world")
    assert md5_hash(temp_file_path1) != md5_hash(temp_file_path2)
