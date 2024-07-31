# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QHeaderView,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTabWidget, QWidget)

from src.gui.components.ImageTreeView import ImageTreeView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionselect_image_file = QAction(MainWindow)
        self.actionselect_image_file.setObjectName(u"actionselect_image_file")
        self.actionselect_directory = QAction(MainWindow)
        self.actionselect_directory.setObjectName(u"actionselect_directory")
        self.actionselect_csv_file = QAction(MainWindow)
        self.actionselect_csv_file.setObjectName(u"actionselect_csv_file")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 1, 1, 1, 1)

        self.imageLabel = QLabel(self.centralwidget)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.imageLabel, 0, 1, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.dirTab = QWidget()
        self.dirTab.setObjectName(u"dirTab")
        self.gridLayout_2 = QGridLayout(self.dirTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.fileTreeView = ImageTreeView(self.dirTab)
        self.fileTreeView.setObjectName(u"fileTreeView")

        self.gridLayout_2.addWidget(self.fileTreeView, 0, 0, 1, 1)

        self.tabWidget.addTab(self.dirTab, "")
        self.otherTab = QWidget()
        self.otherTab.setObjectName(u"otherTab")
        self.tabWidget.addTab(self.otherTab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 2, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.fileMenu = QMenu(self.menubar)
        self.fileMenu.setObjectName(u"fileMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.fileMenu.menuAction())
        self.fileMenu.addAction(self.actionselect_image_file)
        self.fileMenu.addAction(self.actionselect_directory)
        self.fileMenu.addAction(self.actionselect_csv_file)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionselect_image_file.setText(QCoreApplication.translate("MainWindow", u"select image file", None))
        self.actionselect_directory.setText(QCoreApplication.translate("MainWindow", u"select directory", None))
        self.actionselect_csv_file.setText(QCoreApplication.translate("MainWindow", u"select csv file", None))
        self.imageLabel.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247Label", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dirTab), QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u76ee\u5f55", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.otherTab), QCoreApplication.translate("MainWindow", u"\u5f85\u5b9a", None))
        self.fileMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
    # retranslateUi

