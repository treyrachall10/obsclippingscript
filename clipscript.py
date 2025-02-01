import obspython as obs
import os
import datetime

operatingSystem = os.name
homeDir = os.path.join(os.path.expanduser("~"), "Videos")

if not os.path.isdir(homeDir):
    raise ValueError(f"Directory does not exist: {homeDir}")

def startRecording():
    obs.obs_frontend_recording_start()


def stopRecording():
    obs.obs_frontend_recording_stop()
# gets current file path
    oldPath = getOldFilePath()
# gets new file name
    newFilePath = getNewFileName()
    assignFileName(newFilePath, oldPath)


# gets name of file
def getNewFileName():
    category = input("input category")
    moveName = input("input moveName")
    newFilePath = checkFileName(category, moveName)
    return newFilePath

# checks if file name is already taken
def checkFileName(category, moveName):
    counter = 1
    while True:
        # arranges new file name
        newName = f"{category}_{moveName}_{counter}"
        # arranges file name
        newFilePath = getNewFilePath(newName)
        # if name taken then increment the counter
        if not os.path.exists(newFilePath):
            return newFilePath
        counter += 1

# assigns new file name
def assignFileName(newName, oldPath):
    os.rename(oldPath, newName)

# returns the current file path
def getOldFilePath():
    currentTime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    oldPath = os.path.join(homeDir, f"{currentTime}.mp4")
    return oldPath

# returns the updated file path
def getNewFilePath(newName):
    return os.path.join(homeDir, f"{newName}.mp4")