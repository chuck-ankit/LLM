import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
logging.info("Hello everyone welcome to Interviw-Questions-Creator project.")

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "prompt.py",
    ".env",
    "setup.py",
    "research/trails.ipynb",
    "app.py"
]