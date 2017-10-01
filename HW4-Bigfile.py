#Bigfile Homework
#WEIWEI SU
#U17420699
#Last: 9/30/2017

import os

def bigfiles():
    #prompt argument with dir path, exit if wrong path is entered
    while 1:
        basepth = input("Enter a directory path (Must be valid): ")
        if os.path.isdir(basepth):
            print ("Searching %s ...." %basepth)
            break
        else:
            print ("Not a Valid path! Try Again")

    #Define Bigfile List
    big = []

    #Search
    for item in os.listdir(basepth):
        item = basepth + "/" + item
        #make recursive if path is exist and is a directory (assume the basepth folder have subfolders inside)
        if os.path.isdir(item):
            bigfiles(item)
        else:
            itemsize = os.path.getsize(item)
            #find file size more than 100MB
            if itemsize > 100000000:
                big.append((item, itemsize))

    #Found! Delete it
    if big is not None:
        for item in big:
            print ("File found, PATH: %s" %item[0])
            print ("deleting....")
            os.remove(item[0])
            print ("File Deleted.")
