import os
import datetime

def getEntryField(recordingPath):
    category = input("Enter Name of category Ex: exciting, nonexciting")
    move = input("Enter Name of Move Ex: submission, sweep, takedown")
    finalFilePath = getNewFileName(recordingPath, category, move)
    return finalFilePath

# gets name of file
def getNewFileName(recordingPath, category, move):
    newFilePath = checkFileName(recordingPath, category, move)
    return newFilePath

# returns the updated file path
def getNewFilePath(recordingPath, newName):
    return os.path.join(recordingPath, f"{newName}.mp4")

# assigns new file name
def assignFileName(oldPath, newName):
    os.rename(oldPath, newName)

# checks if file name is already taken
def checkFileName(recordingPath, category, moveName):
    counter = 1
    while True:
        # arranges new file name
        newName = f"{category}_{moveName}_{counter}"
        # arranges file name
        newFilePath = getNewFilePath(recordingPath, newName)
        # if name taken then increment the counter
        if not os.path.exists(newFilePath):
            return newFilePath
        counter += 1
