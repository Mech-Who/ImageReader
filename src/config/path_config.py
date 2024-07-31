from pathlib import Path
from dataclasses import dataclass

@dataclass
class PathConfig:
    PROJECT_ROOT = Path(r"D:\Project\MyProjects\ImageReader")
    ASSETS_ROOT = Path(r"D:\Project\MyProjects\ImageReader\assets")
    SRC_ROOT = Path(r"D:\Project\MyProjects\ImageReader\src")
    UI_ROOT = Path(r"D:\Project\MyProjects\ImageReader\src\gui\ui")
    GEN_ROOT = Path(r"D:\Project\MyProjects\ImageReader\src\gui\gen")
