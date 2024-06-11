import sys
from PySide6.QtWidgets import QApplication

# 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
app = QApplication(sys.argv)

# 初始化并展示我们的界面组件
window = ()
window.show()

# 结束QApplication
sys.exit(app.exec_())
