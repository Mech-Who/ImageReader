import os
import csv
from pathlib import Path
from typing import List, Dict, Tuple, Union

import pandas as pd
# 任何一个PySide界面程序都需要使用QApplication
# 我们要展示一个普通的窗口，所以需要导入QWidget，用来让我们自己的类继承
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QMainWindow, QFileDialog, QGraphicsScene, QFileSystemModel
from PySide6.QtCore import Qt, Slot, Signal, QModelIndex

# 导入我们生成的界面
from src.gui.gen.Ui_MainWindow import Ui_MainWindow
from src.config.path_config import PROJECT_ROOT, ASSETS_ROOT
from src.utils.file import getFileType, create_top_item, show_img_in_graphics_view

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
        self.dir_path = Path(dir_name)
        self.dir_files = [self.dir_path / file
                          for file in os.listdir(self.dir_path)]
        tree = self.ui.fileTreeView
        # 设置数据
        self.tree_model = QFileSystemModel()
        self.tree_model.setRootPath(str(self.dir_path.absolute()))
        tree.setModel(self.tree_model)
        tree.setRootIndex(self.tree_model.index(str(self.dir_path.absolute())))

    @Slot(QModelIndex)
    def on_fileTreeView_expanded(self, index):
        tree = self.ui.fileTreeView
        file_info = tree.model().fileInfo(index)
        file_name = file_info.absoluteFilePath()
        print(file_name)

    @Slot(QModelIndex)
    def on_fileTreeView_clicked(self, index):
        tree = self.ui.fileTreeView
        file_info = tree.model().fileInfo(index)
        file_name = Path(file_info.absoluteFilePath())
        if file_name.suffix.lower() in ['.jpg', '.jpeg', '.gif', '.png']:
            show_img_in_graphics_view(self.ui.graphicsView, file_name)
            self.ui.imageLabel.setText(f"{file_name.stem}")

    @Slot()
    def on_actionselect_csv_file_triggered(self):
        # TODO: 实现思路上还有问题，有待调整，因为时间原因，所以暂时先不实现。
        file_name, _ = QFileDialog.getOpenFileName(self, "选择图片",
                                                   dir=str(PROJECT_ROOT),
                                                   filter="csv文件 (*.csv)")
        file_path = Path(file_name)
        # create model
        self.model = QStandardItemModel()
        dict_reader = csv.DictReader(file_name)
        data_list = []
        for row in dict_reader:
            image_name = row["Image"]
            label = row["Label"]
            label_number = row["Label_Number"]
            item = QStandardItem()
            item.setText(image_name)
            item.setData(f"{label}-{label_number}")
            data_list.append(item)
        self.model.appendRow(data_list)
        # set model
        self.ui.fileTreeView.setModel(self.model)
