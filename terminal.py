import sys
from utils import getEntryField, assignFileName

oldPath = sys.argv[1]
recordingFolder = sys.argv[2]

finalFilePath = getEntryField(recordingFolder)
assignFileName(oldPath, finalFilePath)

