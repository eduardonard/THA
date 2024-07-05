"""
Tests for the `sync` module.
"""
import random
import string
import pytest
import modules.sync as sync


def generate_random_string(length):
    """
    Generates a random string of the specified length.

    Parameters:
        length (int): The length of the random string to generate.

    Returns:
        str: A randomly generated string consisting of uppercase and lowercase letters.
    """
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


RANDOM_CONTENT = generate_random_string(10)
RANDOM_FILE_NAME = generate_random_string(10)


@pytest.fixture
def setup_test_folders(tmpdir):
    source_dir = tmpdir.mkdir("source")
    replica_dir = tmpdir.mkdir("replica")

    # Create a test file in the source directory
    source_file = source_dir.join(f"{RANDOM_FILE_NAME}.txt")
    source_file.write(RANDOM_CONTENT)

    return source_dir, replica_dir


def test_create_or_update(setup_test_folders):
    source_dir, replica_dir = setup_test_folders

    sync.create_or_update(str(source_dir), str(replica_dir))

    # Check if the file was copied to the replica
    replica_file = replica_dir.join(f"{RANDOM_FILE_NAME}.txt")
    assert replica_file.exists()

    # Check the content of the copied file
    with open(str(replica_file), "r", encoding="utf-8") as f:
        content = f.read()
        assert content == RANDOM_CONTENT


def test_delete_files(setup_test_folders):
    source_dir, replica_dir = setup_test_folders

    sync.delete_files(str(source_dir), str(replica_dir))

    # Check if the file was deleted from the replica
    replica_file = replica_dir.join(f"{RANDOM_FILE_NAME}.txt")
    assert not replica_file.exists()
