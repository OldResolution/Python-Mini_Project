# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_dashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
class Ui_dashboard_window(object):
    def setupUi(self, dashboard_window):
        if not dashboard_window.objectName():
            dashboard_window.setObjectName(u"dashboard_window")
        dashboard_window.resize(800, 600)
        self.centralwidget = QWidget(dashboard_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout.addWidget(self.widget)

        dashboard_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(dashboard_window)

        QMetaObject.connectSlotsByName(dashboard_window)
    # setupUi

    def retranslateUi(self, dashboard_window):
        dashboard_window.setWindowTitle(QCoreApplication.translate("dashboard_window", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("dashboard_window", u"PushButton", None))
    # retranslateUi

