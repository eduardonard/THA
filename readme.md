# Folder Synchronization Script

## Overview

This script is designed to keep a `replica` folder in sync with a `source` folder. It ensures that the contents of the `replica` always mirror those of the `source` by periodically checking for any discrepancies and performing the necessary file operations (copying, updating, or deleting) to achieve synchronization.

## Usage

### Requirements
- **Python 3**: Ensure Python 3 is installed on your system.

### Running the Script

To run the script, use the following command:
```bash
python3 sync_folders.py [-h] <source_folder> <replica_folder> <interval> <log_file>
```

#### Example Usage

If you want to quickly test the script, follow these steps:

1. **Create Directories**:
    ```bash
    mkdir source replica logs
    ```

2. **Create a Test File**:
    ```bash
    echo "works indeed" >> ./source/works.txt
    ```

3. **Run the Script**:
    ```bash
    python3 sync_folders.py ./source ./replica 300 ./logs/log_file.log
    ```

This will synchronize the `replica` folder with the `source` folder every 300 seconds (5 minutes) and log the operations to `./logs/log_file.log`.

4. **Clean Up**:
    To remove the test directories, use:
    ```bash
    rm -rf source replica logs
    ```

### Automated Testing with `pytest`

To make sure the script works as expected, you can run automated tests. The script includes comprehensive tests that cover most of its functionalities. These tests verify various aspects such as file synchronization, file updates, deletions, and logging.

1. **Install `pytest`**:
    ```bash
    pip install pytest
    ```

2. **Run Tests**:
    Simply run:
    ```bash
    pytest
    ```
    This will execute all the test cases located in the script or in test files following the `pytest` naming conventions. The tests are designed to simulate different scenarios and ensure the synchronization logic is robust and reliable.

#### Test Coverage

The `pytest` tests are structured to cover the following aspects of the script:

- **File Change**: Ensures files differences
- **File Copying**: Ensures new files from the `source` are copied to the `replica`.
- **File Updating**: Checks that updated files in the `source` are mirrored in the `replica`.
- **File Deletion**: Verifies that files removed from the `source` are also deleted from the `replica`.


## Implementation

### Why MD5

- Checksum Verification: MD5 can be used to generate a checksum (hash value) for a file. When you compute the MD5 hash of a file, you get a unique fingerprint of that file's contents. If the file is altered in any way, even by a single bit, the resulting hash will be different.
- Quick Computation: MD5 is relatively fast to compute compared to some other cryptographic hash functions. This makes it efficient for checking large files or many files in bulk.

### `shutil` Library:

- Simplifies file operations like copying, moving, renaming, and deleting files and directories.
- Provides functions for managing directory trees, making recursive operations easy (`shutil.copytree`, `shutil.rmtree`).
- Handles platform-specific file and path conventions, ensuring cross-platform compatibility.
- Supports atomic operations like moving files (`shutil.move`), ensuring operations complete reliably.

### `argparse` Library:

- Parses command-line arguments and options passed to a Python script.
- Automatically generates help messages and usage information based on defined arguments.
- Supports various argument types (positional, optional, flag) with default values and validation.
- Integrates seamlessly with Python scripts, allowing easy retrieval and usage of parsed arguments within the script's logic.