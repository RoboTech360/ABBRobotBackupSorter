# ============================================================
# ABB robot backup sorting script.
# 
# This script is primarily designed to sort out backups of ABB robots
# deep inside a file tree and by identifying and zipping the backup folders. 
# The machine backup folders are identified by the presence of 
# a "BACKINFO" folder and a "system.xml" file within the folder.
#
# This script can be easily tweaked and adapted for other cases 
# where specific folders or files need to be identified, zipped, 
# and optionally deleted. It serves as a reference for organizing 
# backup data efficiently by adjusting the search criteria.
#
# Author: Robotech360
# ============================================================
# revision history:
# // ver 5. - added logging info setup, a log file will be crearted.
# // ver 4. - added user confirmation for deleting the original backup folders.
# // ver 3. - stopped recurse into subdirectories once valid backup is found.
# // ver 2. - checks for system.xml file along with BACKINFO.
# // ver 1. - checks for BACKINFO and zips and deletes the parent backup folder.

import os
import zipfile
import shutil
import logging
import sys

def setup_logging():
    logging.basicConfig(filename="backupsorting_log.txt", level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")
    
def find_and_zip_backup_folders(base_path, delete_after_zip=False):
    # ensure the base path exists
    if not os.path.exists(base_path):
        logging.error(f"The base path {base_path} does not exist.")
        print(f"Error: The base path {base_path} does not exist.")
        return

    # walk through directory tree starting from base_path
    for root, dirs, files in os.walk(base_path):
        try:
            # debugging output: check the current folder and its directories
            print(f"Checking folder: {root}")
            logging.info(f"Checking folder: {root}")
            print(f"Subdirectories in this folder: {dirs}")
            # logging.info(f"Subdirectories in this folder: {dirs}") //too much
            
            # check if 'BACKINFO' exists in the current directory
            if 'BACKINFO' in dirs:
                # additional check if 'system.xml' exists too
                if 'system.xml' in files:
                    print(f"Found valid machine backup folder in: {root}")
                    logging.info(f"Found valid machine backup folder: {root}")
                    
                    # mark parent folder as the backup folder
                    parent_folder = root
                    zip_path = f"{parent_folder}.zip"
                    
                    # check if zip file already exists
                    if os.path.exists(zip_path):
                        print(f"Zip file already exists: {zip_path}")
                        logging.warning(f"Zip file already exists: {zip_path}")
                        continue  # skip
                    
                    # zip the backup folder
                    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                        for foldername, subfolders, filenames in os.walk(parent_folder):
                            for filename in filenames:
                                file_path = os.path.join(foldername, filename)
                                zipf.write(file_path, os.path.relpath(file_path, parent_folder))

                    # once zip file is created, delete the original backup folder (if user chose to)
                    if os.path.exists(zip_path) and delete_after_zip:
                        shutil.rmtree(parent_folder)
                        logging.warning(f"Zipped and deleted folder: {parent_folder}")
                        print(f"Zipped and deleted folder: {parent_folder}")
                    elif os.path.exists(zip_path):
                        logging.info(f"Zipped folder: {parent_folder}, but folder was not deleted.")
                        print(f"Zipped folder: {parent_folder}, but folder was not deleted.")
                
                else:
                    print(f"No system.xml found in: {root}")
                
                # stop walking into subdirectories of backup folder
                dirs[:] = []  # clear dirs list 
                
            else:
                print(f"No BACKINFO folder in: {root}")
        except Exception as e:
            logging.error(f"Error processing folder {root}: {e}")
            print(f"Error processing folder {root}: {e}")

# // main script starts here.
# setup logging
setup_logging()

# //
# main function to accept command-line arguments
if __name__ == "__main__":
    # check for basepath argument
    if len(sys.argv) < 2:
        print("Error: Please provide the base path as an argument.")
        logging.warning("Error: Please provide the base path as an argument.")
        sys.exit(1)

    base_path = sys.argv[1]  # First argument is the base path
# //

# Ask the user if they want to delete the folders after zipping them
user_input = input("Do you want to delete the folders after zipping them? (yes/no): ").strip().lower()
delete_folders = True if user_input == 'yes' else False

# // Specify the base path to search for backup folders.if not running with batch file.
# // Raw string to handle backslashes or using environment variable for username
# base_path = r"C:\Users\malik\Desktop\Code_Playground\test"
# base_path = f"C:\\Users\\{os.environ['USERNAME']}\\Desktop\\Code_Playground\\test"

# Call the function with the appropriate delete_after_zip value
find_and_zip_backup_folders(base_path, delete_after_zip=delete_folders)

# // end of module

