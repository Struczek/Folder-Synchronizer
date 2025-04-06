import argparse
import time
from utils.logger import setup_logger
from controllers.sync_controller import sync_folders
import logging

def main():
    parser = argparse.ArgumentParser(description="Folder Synchronization Script")
    parser.add_argument("source", help="Path to the source folder")
    parser.add_argument("replica", help="Path to the replica folder")
    parser.add_argument("interval", type=int, help="Synchronization interval in seconds")
    parser.add_argument("log_file", help="Path to the log file")
    args = parser.parse_args()

    setup_logger(args.log_file)

    try:
        while True:
            logging.info("Starting synchronization...")
            sync_folders(args.source, args.replica)
            logging.info("Synchronization complete.")
            time.sleep(args.interval)
    except KeyboardInterrupt:
        logging.info("Synchronization interrupted by user.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
