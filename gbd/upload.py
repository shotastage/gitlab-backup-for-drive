from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class FileUpload():

    def __init__(self):
        self._gauth = GoogleAuth().CommandLineAuth()
        self._drive = GoogleDrive(self._gauth)
        