## ABBRobotBackupSorter
python based program to find and zip all ABB robot backups in a file tree.
ABB robot backup sorting script.

This script is primarily designed to sort out backups of ABB robots
deep inside a file tree and by identifying and zipping the backup folders. 
The machine backup folders are identified by the presence of 
a "BACKINFO" folder and a "system.xml" file within the folder.
a log file is created for looging all steps and events.
This script can be easily tweaked and adapted for other cases 
where specific folders or files need to be identified, zipped, 
and optionally deleted. It serves as a reference for organizing 
backup data efficiently by adjusting the search criteria.

Author: Robotech360

### revision history / release notes:
- ver 1.6 - added fuction to take a bsaepath argument from command line.
- ver 1.5 - added logging info setup, a log file will be crearted.
- ver 1.4 - added user confirmation for deleting the original backup folders.
- ver 1.3 - stopped recurse into subdirectories once valid backup is found.
- ver 1.2 - checks for system.xml file along with BACKINFO.
- ver 1.1 - checks for BACKINFO and zips and deletes the parent backup folder.

## how to use:
## option 1: Run the Executable with the Batch File
  Download the ABBRobotBackupSorter_v1.6.exe from the Releases folder. In the Releases folder, you'll find the example batch file run_ABBRobotBackupSorter_v1.6.bat.
  The batch file is pre-configured to run the executable with a specified base path. By default, it uses:
  
  SET BACKUP_PATH=C:\Users\%USERNAME%\Desktop\Code_Playground\test
  
  ouble-click the run_ABBRobotBackupSorter_v1.6.bat file to execute the program. The batch file will launch the executable and pass the base path as an argument.
  
## option 2: Run the Python Script Manually (If Python is Installed)
  If you have Python installed on your system, you can choose to run the Python script manually.
  Download the Python script from the /src folder.
  Open the batch file and modify it to run the Python script instead of the executable:
  Uncomment the line to run the Python script:
  
  REM python ABBRobotBackupSorter_v1.6.py "%BACKUP_PATH%"
  
  Comment the line that runs the executable: 
  
  REM start "" "C:\path\to\your\dist\ABBRobotBackupSorter_v1.6.exe" "%BACKUP_PATH%"
  
  After modifying the batch file, double-click it to run the Python script with the defined base path.

## Option 3: Run the Script in Debug Mode
  If you want to run the script in debug mode, you can do so by manually setting the base path in the script.
  Open the Python script (ABBRobotBackupSorter_v1.6.py) from /src folder In the script, comment the section that handles command-line arguments
  Set the base path directly in the script manually at the end. 
  Run the script manually from the command line or using an IDE (such as Visual Studio Code or PyCharm) for debugging.

