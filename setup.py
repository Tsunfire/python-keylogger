from setuptools import setup

APP = ['keylogger.py'] # points to your main python file
DATA_FILES = []
OPTIONS = {
    'packages': ['pynput'] # include your other dependencies here
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)