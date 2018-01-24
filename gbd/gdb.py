#!/usr/bin/env python3

import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def main():
    print("GDB!")


def read_backups():
    pass

def create_gitlab_backup():
    os.system("sudo gitlab-rake gitlab:backup:create")


class FileUpload():

    def __init__(self, save_to):
        self._gauth = GoogleAuth().CommandLineAuth()
        self._drive = GoogleDrive(self._gauth)
        self._upload_to = save_to


    def upload(self):
        f = self._drive.CreateFile(
            {
                'title': 'backup_file',
                'mimeType': 'application/x-tar',
                'parents': [
                    {'kind': 'drive#fileLink', 'id': self._upload_to}
                ]
            }
        )
        f.SetContentFile('backup_file')
        f.Upload()
