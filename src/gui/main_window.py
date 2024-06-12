import os
from pathlib import Path
from typing import List, Dict, Tuple, Union

# 任何一个PySide界面程序都需要使用QApplication
# 我们要展示一个普通的窗口，所以需要导入QWidget，用来让我们自己的类继承
from PySide6.QtGui import QImage, QIcon
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QGraphicsScene, QTreeWidgetItem
from PySide6.QtCore import Qt, Slot, Signal

# 导入我们生成的界面
from src.gui.gen.Ui_MainWindow import Ui_MainWindow
from src.config.path_config import PROJECT_ROOT, ASSETS_ROOT
from src.utils.file import getFileType, create_top_item

# 继承QWidget类，以获取其属性和方法


class MainWindow(QMainWindow):
    select_image = Signal()
    select_dir = Signal()
    select_csv = Signal()

    def __init__(self):
        super(MainWindow, self).__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.class_init()
        self.ui_init()
        self.slot_signal_init()

    def class_init(self):
        pass

    def ui_init(self):
        pass

    def slot_signal_init(self):
        pass

    # 槽函数
    @Slot()
    def on_actionselect_image_file_triggered(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "选择图片",
                                                   dir=str(PROJECT_ROOT),
                                                   filter="图片文件 (*.jpg *.gif *.png *.jpeg)")
        print(f"open file: {file_name}")
        file_path = Path(file_name)
        self.ui.imageLabel.setText(f"{file_path.stem}")
        scene = QGraphicsScene()
        scene.addPixmap(str(file_path))
        self.ui.graphicsView.setScene(scene)
        self.ui.graphicsView.fitInView(
            scene.sceneRect(),
            Qt.AspectRatioMode.KeepAspectRatio)
        self.ui.graphicsView.show()

    @Slot()
    def on_actionselect_directory_triggered(self):
        dir_name = QFileDialog.getExistingDirectory(
            self, "选择图片目录", dir=str(PROJECT_ROOT))
        # print(f"open dir: {dir_name}")
        self.dir_path = Path(dir_name)
        self.dir_files = [self.dir_path / file 
                          for file in os.listdir(self.dir_path)]
        # print(self.dir_files[0])
        tree = self.ui.fileTreeWidget
        top_item = QTreeWidgetItem(tree)
        top_item.setText(0, str(self.dir_path.stem))
        top_item.setText(1, getFileType(self.dir_path))
        top_item.setIcon(0, QIcon(str(ASSETS_ROOT / "icon/dir-folder.png")))

        self.create_top_item(top_item, self.dir_files)

        tree.addTopLevelItem(top_item)
        # tree.expandAll()
