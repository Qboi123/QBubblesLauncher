import json
import os
import platform
import time
import urllib.request
from io import BytesIO
from typing import Optional

if platform.system() == "Windows":
    TEMP_DIR = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp\\"
elif platform.system() == "Linux":
    TEMP_DIR = f"/home/{os.getlogin()}/.temp/"
else:
    raise OSError(f"Platform is unsupported")


class Updater(object):
    def __init__(self):
        self.hasUpdates = False

    def check_updates(self):
        update_available = False
        # urllib.request.urlopen("")
        fp: Optional[BytesIO] = None

        data = json.loads(fp.read())
        if data["updatetime"] < time.time():
            update_available = True
            url = data["url"]

        if update_available:
            self.hasUpdates = True

            # noinspection PyUnboundLocalVariable
            self.download(url)

    def download(self, url):
        gui = UpdaterGUI()

        while download.is_downloading():


    def update(self):
        if not self.hasUpdates:
            return


class UpdaterGUI():
    pass
