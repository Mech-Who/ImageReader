from pathlib import Path

def getFileType(filename: str|Path) -> str:
    if not isinstance(filename, Path):
        filename = Path(filename)
    if filename.is_dir():
        return "dir"
    else:
        return "file"
