from pathlib import Path
import sys
import platform
import os
import time
import datetime

def CompareDirectories(path1, path2):
    for item1 in path1.iterdir():
        found = False
        for item2 in path2.iterdir():
            if item1.name == item2.name:
                found = True
                if item1.is_dir():
                    CompareDirectories(item1,item2)
                else:
                    time1 = datetime.datetime.fromtimestamp(item1.stat().st_mtime)
                    time2 = datetime.datetime.fromtimestamp(item2.stat().st_mtime)
                    difference = time1 - time2
                    # A little ugly solution here, but sometimes the last modified time differs 1 second or about one hour even if they were modified at the same time. The latter is probably related to the summer time and different memory technologies. Let's ignore those.
                    if difference > datetime.timedelta(0,2) and not (difference > datetime.timedelta(0,58,0,0,59) and difference <= datetime.timedelta(0,0,0,0,0,1)):
                        print("diff mod time\t" + str(item1) + " | " + str(difference))
                        
        if found == False:
            print("not found\t" + str(item1))
            
def main():
    path1 = sys.argv[1]
    path2 = sys.argv[2]
    CompareDirectories(Path(path1), Path(path2))
    
main()