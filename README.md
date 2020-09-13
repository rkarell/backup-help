# BackupHelp
A small python command line tool to compare files and folders.

## What is does

The program takes two folders as arguments. The first folder is compared with the second one. If a file in the first folder is not found in the second folder, or if it has a different last modified time, the name of the file is returned. In case of different last modified time, also the difference in the time is returned. All subfolders are automatically checked too.

## Use case
When backing up your files, this tool can be used to check which of your files are new or modified. Give the folder that you want to backup as the first argument and the backup folder as the second argument.

## How to use

    python BackupHelp.py path/to/folder1 path/to/folder2