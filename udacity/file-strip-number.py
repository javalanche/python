import os

def renameFile():
    #(1) get file names from a folder
    fileList = os.listdir(r"C:\Users\jf732h\Dropbox\programmingFoundationsWithPython\lesson1\prank")
    print (fileList)
    savedPath = os.getcwd()
    # print(savedPath)

    os.chdir(r"C:\Users\jf732h\Dropbox\programmingFoundationsWithPython\lesson1\prank")
    #(2) for each file, remane file
    for fileName in fileList:
        print("Old Name - "+fileName)
        print("New Name - "+fileName.translate(None, "0123456789"))
        os.rename(fileName, fileName.translate(None, "0123456789"))
    os.chdir(savedPath)
renameFile()
