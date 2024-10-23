import os
import logging
import time

# Setup logging
logging.basicConfig(
                    level=logging.INFO,
                    format='%(asctime)s - %(message)s')


def process_existing_folders(path):
    # List all subfolders in the 'unprocessed/' directory
    subfolders = [f.path for f in os.scandir(path) if f.is_dir()]

    if not subfolders:
        logging.info(f"No folders found in: {path}")
        return


    # Log each folder found
    for folder in subfolders:
        logging.info(f"Detected folder: {folder}")

    # Log the first folder for processing
    first_folder = subfolders[0]
    logging.info(f"First folder for processing: {first_folder}")

    # Placeholder for the processing logic
    # process_folder(first_folder)  # Uncomment and implement this later


if __name__ == "__main__":
    folder_to_monitor = os.path.join(os.getcwd(), "..", "unprocessed")

    while True:
        process_existing_folders(folder_to_monitor)
        logging.info("Waiting 10 seconds before next check...")
        time.sleep(10)  # Wait 10 seconds before the next check
