import sys

# 任何一个PySide界面程序都需要使用QApplication
# 我们要展示一个普通的窗口，所以需要导入QWidget，用来让我们自己的类继承
from PySide6.QtWidgets import QApplication, QMainWindow

# 导入我们生成的界面
from src.gui.gen.Ui_MainWindow import Ui_MainWindow

# 继承QWidget类，以获取其属性和方法
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)

    # 初始化并展示我们的界面组件
    window = MainWindow()
    window.show()

    # 结束QApplication
    sys.exit(app.exec_())