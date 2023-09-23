"""Write a Python program to sort files by date."""

import os,time

if __name__ == "__main__": 
    #Considering for current directory
    files = []

    for dirpath,dirnames,filenames in os.walk(os.getcwd()):
        for file in filenames:
            path = os.path.join(dirpath,file)
            files.append(path)

    files_dates = {}
    for file in files:
        t = time.ctime(os.path.getctime(file))
        files_dates[file] = t

    files_sorted = sorted(files_dates.items(), key = lambda x : x[1])

    print("\n List of files sorted by creation time: ")
    for (key,value) in files_sorted:
        print("{} {}".format(key,value))

    

    