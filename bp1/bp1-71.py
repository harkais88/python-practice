"""Write a Python program to get a directory listing, sorted by creation date."""

import os,time

if __name__ == "__main__": 
    #Considering for current directory
    dirs = []

    dir_url = os.path.normpath("C:\\Users\\arka_\\Documents\\Python Scripts")

    for dirpath,dirnames,filenames in os.walk(dir_url):
        for dir in dirnames:
            path = os.path.join(dirpath,dir)
            dirs.append(path)

    dirs_dates = {}
    for dir in dirs:
        t = time.ctime(os.path.getctime(dir))
        dirs_dates[dir] = t

    dirs_sorted = sorted(dirs_dates.items(), key = lambda x : x[1])

    print("\n List of files sorted by creation time: ")
    for (key,value) in dirs_sorted:
        print("{} {}".format(key,value))