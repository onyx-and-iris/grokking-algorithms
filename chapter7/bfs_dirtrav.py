import logging
from collections import deque
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

scripts_path = Path.home() / "scripts"


def files_with_extension(ext):
    queue = deque()
    queue += scripts_path.glob("*")

    while queue:
        item = queue.popleft()

        # if it is a file and has extension ext then print
        if item.is_file() and item.suffix == ext:
            print(item)

        # otherwise add directory items to the queue
        else:
            queue += item.glob("*")


files_with_extension(".sh")
