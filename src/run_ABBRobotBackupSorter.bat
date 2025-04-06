@echo off
REM Batch file to run the Python script ABBRobotBackupSorter

REM Define the base path (main folder where all the backup exists.)
SET BACKUP_PATH=C:\Users\%USERNAME%\Desktop\Code_Playground\test

REM Run the Python script with the backup path as an argument
REM python ABBRobotBackupSorter_v1.6.py "%BACKUP_PATH%"

REM Run the executable with the backup path as an argument
start "" "C:\path\to\your\dist\ABBRobotBackupSorter_v1.6.exe" "%BACKUP_PATH%"

REM Pause to keep the window open after execution
pause
