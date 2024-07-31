import logging
from typing import Union

from PySide6.QtCore import Qt, Signal, Slot, QModelIndex
from PySide6.QtWidgets import QTreeView

logger = logging.getLogger(__file__)

class ImageTreeView(QTreeView):
    show_previous = Signal(QModelIndex)
    show_next = Signal(QModelIndex)

    def __init__(self, parent=None):
        super(ImageTreeView, self).__init__(parent)
        self.current_index: QModelIndex = None
        # 初始化你的自定义组件

    def keyPressEvent(self, event):
        # 重写keyPressEvent来处理键盘事件
        if event.key() == Qt.Key_Up or event.key() == Qt.Key_Left:
            self.show_previous_image()
        elif event.key() == Qt.Key_Down or event.key() == Qt.Key_Right:
            self.show_next_image()
        else:
            super().keyPressEvent(event)

    def show_previous_image(self):
        # 切换到上一张图片的逻辑
        print("Key_Up pressed")
        sibling = self.current_index.sibling(self.current_index.row() - 1, self.current_index.column())
        if sibling.row() == -1:
            logger.debug("index is already the first(1)!")
            return
        self.current_index = sibling
        self.show_previous.emit(self.current_index)

    def show_next_image(self):
        # 切换到下一张图片的逻辑
        print("Key_Down pressed")
        sibling = self.current_index.sibling(self.current_index.row() + 1, self.current_index.column())
        if sibling.row() == -1:
            logger.debug("index is already the last(-1)!")
            return
        self.current_index = sibling
        self.show_next.emit(self.current_index)
