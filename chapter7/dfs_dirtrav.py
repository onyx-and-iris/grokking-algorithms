import logging
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

EXT = ".rb"

scripts_path = Path.home() / "scripts"


def files_with_extension(directory):
    for item in directory.glob("*"):
        # if item is a file and has extension EXT then print
        if item.is_file():
            if item.suffix == EXT:
                print(item)

        # otherwise pass directory to recursive call
        else:
            files_with_extension(item)


files_with_extension(scripts_path)
