
import os
import shutil
import csv

def FilePath(msg):
    filePathExists = False
    while filePathExists != True:
        print(msg)
        filePath = input()
        filePathExists = VerifyFilePath(filePath)
        if filePathExists != True:
            print(f"Invalid path. \nPlease, enter a valid file path :")
    
    return filePath

def VerifyFilePath(path):
    return os.path.exists(path)

def ReadFileContent(path):
    content = []
    with open(path) as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            content.append(f"{','.join(row)}")
    return content

def CopyFile(original, target):
    shutil.copyfile(original, target)