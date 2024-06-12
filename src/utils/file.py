from pathlib import Path
from typing import Union


def getFileType(filename: Union[str, Path]) -> str:
    if not isinstance(filename, Path):
        filename = Path(filename)
    if filename.is_dir():
        return "dir"
    else:
        return "file"
