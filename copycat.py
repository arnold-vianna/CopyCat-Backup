import os
import shutil
import logging
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading
import configparser

# Logging
def configure_logging(config):
    level = config['logging'].get('level', 'INFO')
    format_str = config['logging'].get('format', '%(asctime)s - %(message)s')
    datefmt = config['logging'].get('datefmt', '%Y-%m-%d %H:%M:%S')
    logging.basicConfig(level=level, format=format_str, datefmt=datefmt)

logger = logging.getLogger('file-copy')

# Read configuration from INI file
config = configparser.ConfigParser()
config.read('config.ini')  # Assuming the file is named config.ini

# Get configuration values
source_dir = config['DEFAULT'].get('source_dir')
dest_dir = config['DEFAULT'].get('dest_dir')
extensions = config['DEFAULT'].get('extensions', '.txt,.pdf,.jpg,.png,Dockerfile,.zip,.tar,.gz,.bz2').split(',')

# Validate source dir
if not os.path.isabs(source_dir):
    logger.error("Source must be an absolute path")
    exit(1)

# Log startup config
logger.info("Starting file copy watcher")
logger.info("Source: %s", source_dir)
logger.info("Destination: %s", dest_dir)
logger.info("Extensions: %s", extensions)

# Run a new instance of the script in the background
def run_in_background():
    subprocess.Popen(["python", "file_watcher.py"], close_fds=True)

# Copy function running in thread
def copy_file(src, dest):
    try:
        shutil.copy2(src, dest)
        logger.info('Copied %s to %s', src, dest)
    except Exception as e:
        logger.error('Error copying %s: %s', src, e, exc_info=True)

# Event handler class
class FileCopyHandler(FileSystemEventHandler):

    def on_created(self, event):
        if event.is_directory:
            return None

        if event.src_path.endswith(tuple(extensions)):
            filename = os.path.basename(event.src_path)
            dest_path = os.path.join(dest_dir, filename)
            thread = threading.Thread(target=copy_file, args=(event.src_path, dest_path))
            thread.start()
            thread.join()  # Ensure the thread finishes before moving on

            # Check if a specific file is created (change 'example.txt' to your specific file)
            if filename == 'example.txt':
                logger.info('Detected creation of specific file. Restarting in the background...')
                run_in_background()

    def on_modified(self, event):
        if event.is_directory:
            return None

        if event.src_path.endswith(tuple(extensions)):
            filename = os.path.basename(event.src_path)
            dest_path = os.path.join(dest_dir, filename)
            thread = threading.Thread(target=copy_file, args=(event.src_path, dest_path))
            thread.start()
            thread.join()  # Ensure the thread finishes before moving on

    def on_deleted(self, event):
        if event.is_directory:
            return None

        if event.src_path.endswith(tuple(extensions)):
            filename = os.path.basename(event.src_path)
            dest_path = os.path.join(dest_dir, filename)
            try:
                os.remove(dest_path)
                logger.info('Deleted %s', dest_path)
            except Exception as e:
                logger.error('Error deleting %s: %s', dest_path, e, exc_info=True)

# Setup watchdog
event_handler = FileCopyHandler()
observer = Observer()
observer.schedule(event_handler, source_dir, recursive=True)
observer.start()

# The script will continue running in the background
try:
    observer.join()
except KeyboardInterrupt:
    observer.stop()
    logger.info("Script terminated.")
