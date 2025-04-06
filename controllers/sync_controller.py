import os
import shutil
import logging
from pathlib import Path
from utils.hashing import file_hash

def sync_folders(source, replica):
    source = Path(source)
    replica = Path(replica)

    if not source.exists():
        logging.error(f"Source folder does not exist: {source}")
        raise FileNotFoundError(f"Source folder not found: {source}")

    for root, dirs, files in os.walk(source):
        rel_path = os.path.relpath(root, source)
        replica_root = os.path.join(replica, rel_path)

        if not os.path.exists(replica_root):
            os.makedirs(replica_root)
            logging.info(f"Created folder: {replica_root}")

        for file in files:
            try:
                src_file = os.path.join(root, file)
                dst_file = os.path.join(replica_root, file)

                if not os.path.exists(dst_file):
                    shutil.copy2(src_file, dst_file)
                    logging.info(f"Copied new file: {src_file} -> {dst_file}")
                else:
                    if file_hash(src_file) != file_hash(dst_file):
                        shutil.copy2(src_file, dst_file)
                        logging.info(f"Updated file: {src_file} -> {dst_file}")
            except Exception as e:
                logging.error(f"Error syncing file {file}: {e}")

    for root, dirs, files in os.walk(replica, topdown=False):
        rel_path = os.path.relpath(root, replica)
        source_root = os.path.join(source, rel_path)

        for file in files:
            try:
                src_file = os.path.join(source_root, file)
                dst_file = os.path.join(root, file)
                if not os.path.exists(src_file):
                    os.remove(dst_file)
                    logging.info(f"Deleted file: {dst_file}")
            except Exception as e:
                logging.error(f"Error deleting file {file}: {e}")

        for dir in dirs:
            try:
                src_dir = os.path.join(source_root, dir)
                dst_dir = os.path.join(root, dir)
                if not os.path.exists(src_dir):
                    shutil.rmtree(dst_dir)
                    logging.info(f"Deleted folder: {dst_dir}")
            except Exception as e:
                logging.error(f"Error deleting folder {dir}: {e}")
