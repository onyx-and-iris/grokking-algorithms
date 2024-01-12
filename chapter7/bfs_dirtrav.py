import logging
from collections import deque
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

EXT = ".rb"

scripts_path = Path.home() / "scripts"


def files_with_extension(start_directory):
    queue = deque()
    queue.append(start_directory)

    while queue:
        items = queue.popleft()

        for item in items.glob("*"):
            # if item is a file and has extension EXT then print
            if item.is_file():
                if item.suffix == EXT:
                    print(item)

            # otherwise append directory to the queue
            else:
                queue.append(item)


files_with_extension(scripts_path)
