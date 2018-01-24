# -*- encoding:utf-8 -*-
from setuptools import setup, find_packages
import sys

sys.path.append('./gbd')
sys.path.append('./tests')

if __name__ == "__main__":
    setup(
        name = "gbd",
        version='0.0.1',
        author = "Shota Shimazu",
        author_email = "hornet.live.mf@gmail.com",
        packages = find_packages(),
        install_requires=[
            "",
        ],
        entry_points = {
            'console_scripts':[
                'gdb = gdb.gdb:main',
            ],
        },
        description = "GitLab backup for Google Drive",
        long_description = "",
        url = "https://github.com/shotastage/gitlab-backup-for-drive/",
        license = "Apache",
        platforms = ["POSIX", "Windows", "Mac OS X"],
        test_suite = "gdb_test.suite",
    )
