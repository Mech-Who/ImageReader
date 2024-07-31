import sys
import logging
from logging import FileHandler, StreamHandler
from pathlib import Path

from PySide6.QtWidgets import QApplication

from src.gui.main_window import MainWindow
from src.config.log_config import LogConfig
from src.utils.file import mkdir_if_missing

# log
log_config = LogConfig()
log_file = Path(log_config.log_file)
if not log_file.exists():
    mkdir_if_missing(log_file.parent)
    with open(str(log_file.absolute()), "w"):
        pass
logging.basicConfig(level=log_config.log_level, 
                    handlers=[
                        FileHandler(str(log_file), mode='a', encoding='utf-8'),
                        StreamHandler(sys.stdout)
                    ], 
                    format=log_config.format)

logger = logging.getLogger(__file__)

# 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
app = QApplication(sys.argv)

# 初始化并展示我们的界面组件
window = MainWindow()
window.show()

logger.debug("===== Application Start =====")

# 结束QApplication
status = app.exec()

logger.debug("application exit status: %d", status)
logger.debug("===== Application Finish =====")

sys.exit(status)
