"""
This script synchronizes two folders with a given interval.
"""
import time
import argparse
import logging
from modules.sync import sync_directories


def parse_arguments():
    """
    Parse the command line arguments and return the parsed arguments.

    Returns:
        argparse.Namespace: The parsed command line arguments.
    """
    parser = argparse.ArgumentParser(description="Folder Synchronization Script")
    parser.add_argument("source", help="Path to the source folder")
    parser.add_argument("replica", help="Path to the replica folder")
    parser.add_argument("interval", type=int, help="Synchronization interval in seconds")
    parser.add_argument("log_file", help="Path to the log file")
    return parser.parse_args()


def setup_logging(log_file):
    """
    Set up the logging configuration for the application.

    Args:
        log_file (str): The path to the log file.

    Returns:
        None

    This function configures the logging module to write log messages to a file
    specified by `log_file` in append mode. It also adds a console handler to
    display log messages on the console. The log format is set to
    '%(asctime)s - %(levelname)s - %(message)s'. The logging level is set to
    INFO.

    Example:
        >>> setup_logging('logs/app.log')
    """
    logging.basicConfig(
        filename=log_file,
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO,
    )
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

def main():
    """
    The main function that runs the synchronization process in an infinite loop.

    This function parses the command line arguments using the `parse_arguments` function.
    It then retrieves the `source_folder`, `replica_folder`, `interval`, and `log_file`
    from the parsed arguments.

    The `setup_logging` function is called to configure the logging module with the
    specified log file.

    The synchronization process is then performed in an infinite loop. It starts by
    logging the message "Starting synchronization". It then calls the `sync_directories`
    function to synchronize the source folder with the replica folder. After the
    synchronization is complete, it logs the message "Synchronization completed".

    The loop then sleeps for the specified `interval` before starting the next
    iteration.
>
    This function does not take any parameters and does not return any values.
    """
    args = parse_arguments()
    source_folder = args.source
    replica_folder = args.replica
    interval = args.interval
    log_file = args.log_file
    setup_logging(log_file)
    while True:
        logging.info("Starting synchronization")
        sync_directories(source_folder, replica_folder)
        logging.info("Synchronization completed")
        time.sleep(interval)

if __name__ == "__main__":
    main()
