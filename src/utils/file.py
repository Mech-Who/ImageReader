import os
from pathlib import Path
from typing import Union, List

from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QTreeWidgetItem, QGraphicsView, QGraphicsScene
from PySide6.QtCore import Qt

from src.config.path_config import ASSETS_ROOT


def getFileType(filename: Union[str, Path]) -> str:
    if not isinstance(filename, Path):
        filename = Path(filename)
    if filename.is_dir():
        return "dir"
    else:
        return "file"


def create_top_item(top_item: QTreeWidgetItem, files: Union[List[str], List[Path]]) -> None:
    """
    递归建立文件树
    """
    for file_path in files:
        # print(file_path)
        if not isinstance(file_path, Path):
            file_path = Path(file_path)
        child = QTreeWidgetItem()
        child.setText(0, file_path.stem)
        child.setText(1, getFileType(file_path))
        if file_path.suffix in [".png", ".jpg", ".jpeg", ".gif"]:
            child.setIcon(0, QIcon(str(ASSETS_ROOT / "icon/img.png")))
        elif file_path.is_dir():
            child.setIcon(
                0, QIcon(str(ASSETS_ROOT / "icon/dir-folder.png")))
            child_files = [file_path / file
                           for file in os.listdir(str(file_path))]
            create_top_item(child, child_files)
        else:
            child.setIcon(0, QIcon(str(ASSETS_ROOT / "icon/file.png")))
        top_item.addChild(child)

def show_img_in_graphics_view(view: QGraphicsView, img_path: Union[str, Path]) -> None:
    pixmap = QPixmap(str(img_path))
    scene = QGraphicsScene()
    scene.addPixmap(pixmap)
    view.setScene(scene)
    view.fitInView(scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
    view.show()
