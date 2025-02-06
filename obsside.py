import obspython as obs
from utils import stopRecording
import subprocess

hotkeyid = obs.OBS_INVALID_HOTKEY_ID

def stopRecordingAndPassToTerminal(pressed):
    outputHandle = obs.obs_get_output_handle()
    outputSettings = obs.obs_get_settings(outputHandle)
    recordingFolder = obs.obs_data_get_string(outputSettings, "file")
    obs.obs_frontend_recording_stop()
    oldPath = obs.obs_frontend_get_last_recording()
    subprocess.run(["gnome-terminal", "--", "python3", "terminal.py", oldPath, recordingFolder])

def scriptLoad(settings):
    global hotkeyid
    hotkeyid = obs.obs_hotkey_register_frontend("stopRecordingFileChange", "stops recording starts process", stopRecording)
    hotkeyData = obs.obs_data_get_array(settings, "stop_recording_hotkey")
    obs.obs_hotkey_load(hotkeyid, hotkeyData)
    obs.obs_data_array_release(hotkeyData)

def scriptSave(settings):
    global hotkeyid
    hotkeyData = obs.obs_hotkey_save(hotkeyid)
    obs.obs_data_set_array(settings, "stop_recording_hotkey", hotkeyData)
    obs.obs_data_array_release(hotkeyData)
