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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
class Ui_dashboard(object):
    def setupUi(self, dashboard):
        if not dashboard.objectName():
            dashboard.setObjectName(u"dashboard")
        dashboard.resize(849, 616)
        dashboard.setStyleSheet(u"")
        self.centralwidget = QWidget(dashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuContainer = QWidget(self.centralwidget)
        self.LeftMenuContainer.setObjectName(u"LeftMenuContainer")
        self.verticalLayout = QVBoxLayout(self.LeftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuSubContainer = QWidget(self.LeftMenuContainer)
        self.LeftMenuSubContainer.setObjectName(u"LeftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.LeftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.LeftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MenuButton = QPushButton(self.frame)
        self.MenuButton.setObjectName(u"MenuButton")
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/align-justify.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MenuButton.setIcon(icon)
        self.MenuButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.MenuButton, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.LeftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.Homebutton = QPushButton(self.frame_2)
        self.Homebutton.setObjectName(u"Homebutton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Homebutton.sizePolicy().hasHeightForWidth())
        self.Homebutton.setSizePolicy(sizePolicy1)
        self.Homebutton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/feather/icons/feather/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Homebutton.setIcon(icon1)
        self.Homebutton.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.Homebutton)

        self.SettingsButton = QPushButton(self.frame_2)
        self.SettingsButton.setObjectName(u"SettingsButton")
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/chevrons-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SettingsButton.setIcon(icon2)
        self.SettingsButton.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.SettingsButton)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.LeftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.InfoButton = QPushButton(self.frame_3)
        self.InfoButton.setObjectName(u"InfoButton")
        icon3 = QIcon()
        icon3.addFile(u":/feather/icons/feather/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.InfoButton.setIcon(icon3)
        self.InfoButton.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.InfoButton)

        self.LogoutButton = QPushButton(self.frame_3)
        self.LogoutButton.setObjectName(u"LogoutButton")
        icon4 = QIcon()
        icon4.addFile(u":/material_design/icons/material_design/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.LogoutButton.setIcon(icon4)
        self.LogoutButton.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.LogoutButton)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.LeftMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.LeftMenuContainer)

        self.CenterMenuContainer = QWidget(self.centralwidget)
        self.CenterMenuContainer.setObjectName(u"CenterMenuContainer")
        self.verticalLayout_5 = QVBoxLayout(self.CenterMenuContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.CenterMenuSubContainer = QWidget(self.CenterMenuContainer)
        self.CenterMenuSubContainer.setObjectName(u"CenterMenuSubContainer")
        self.verticalLayout_6 = QVBoxLayout(self.CenterMenuSubContainer)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.CenterMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon5 = QIcon()
        icon5.addFile(u":/feather/icons/feather/x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon5)
        self.pushButton_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.pushButton_2, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.stackedWidget = QStackedWidget(self.CenterMenuSubContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.PastSearches = QLabel(self.page_2)
        self.PastSearches.setObjectName(u"PastSearches")
        font = QFont()
        font.setPointSize(13)
        self.PastSearches.setFont(font)
        self.PastSearches.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.PastSearches)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_9 = QVBoxLayout(self.page_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.Information = QLabel(self.page_3)
        self.Information.setObjectName(u"Information")
        self.Information.setFont(font)
        self.Information.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.Information)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_5.addWidget(self.CenterMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.CenterMenuContainer)

        self.MainBodyContainer = QWidget(self.centralwidget)
        self.MainBodyContainer.setObjectName(u"MainBodyContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.MainBodyContainer.sizePolicy().hasHeightForWidth())
        self.MainBodyContainer.setSizePolicy(sizePolicy2)
        self.MainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.MainBodyContainer)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.TitleBar = QWidget(self.MainBodyContainer)
        self.TitleBar.setObjectName(u"TitleBar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.TitleBar.sizePolicy().hasHeightForWidth())
        self.TitleBar.setSizePolicy(sizePolicy3)
        self.TitleBar.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_7 = QHBoxLayout(self.TitleBar)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.TitleBar)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 10))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_12.addWidget(self.label)


        self.horizontalLayout_7.addWidget(self.widget_4)

        self.widget = QWidget(self.TitleBar)
        self.widget.setObjectName(u"widget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy4)
        self.horizontalLayout_11 = QHBoxLayout(self.widget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.Minimize_window = QPushButton(self.widget)
        self.Minimize_window.setObjectName(u"Minimize_window")
        icon6 = QIcon()
        icon6.addFile(u":/feather/icons/feather/window_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Minimize_window.setIcon(icon6)

        self.horizontalLayout_11.addWidget(self.Minimize_window)

        self.Maximize_window = QPushButton(self.widget)
        self.Maximize_window.setObjectName(u"Maximize_window")
        icon7 = QIcon()
        icon7.addFile(u":/feather/icons/feather/square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Maximize_window.setIcon(icon7)

        self.horizontalLayout_11.addWidget(self.Maximize_window)

        self.Close_window = QPushButton(self.widget)
        self.Close_window.setObjectName(u"Close_window")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.Close_window.sizePolicy().hasHeightForWidth())
        self.Close_window.setSizePolicy(sizePolicy5)
        self.Close_window.setMinimumSize(QSize(0, 10))
        icon8 = QIcon()
        icon8.addFile(u":/feather/icons/feather/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Close_window.setIcon(icon8)

        self.horizontalLayout_11.addWidget(self.Close_window)


        self.horizontalLayout_7.addWidget(self.widget, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.TitleBar, 0, Qt.AlignTop)

        self.widget_2 = QWidget(self.MainBodyContainer)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.stackedWidget_2 = QStackedWidget(self.widget_2)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.HomeMain = QWidget()
        self.HomeMain.setObjectName(u"HomeMain")
        self.verticalLayout_7 = QVBoxLayout(self.HomeMain)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.headerContainer = QWidget(self.HomeMain)
        self.headerContainer.setObjectName(u"headerContainer")
        sizePolicy.setHeightForWidth(self.headerContainer.sizePolicy().hasHeightForWidth())
        self.headerContainer.setSizePolicy(sizePolicy)
        self.headerContainer.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_9 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setEnabled(True)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.searchBar = QLineEdit(self.frame_6)
        self.searchBar.setObjectName(u"searchBar")
        sizePolicy4.setHeightForWidth(self.searchBar.sizePolicy().hasHeightForWidth())
        self.searchBar.setSizePolicy(sizePolicy4)
        self.searchBar.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_10.addWidget(self.searchBar)

        self.pushButton = QPushButton(self.frame_6)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy4.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy4)
        icon9 = QIcon()
        icon9.addFile(u":/feather/icons/feather/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon9)

        self.horizontalLayout_10.addWidget(self.pushButton)


        self.horizontalLayout_9.addWidget(self.frame_6, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.headerContainer)

        self.ResultSpace = QSpacerItem(10, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_7.addItem(self.ResultSpace)

        self.progressGame = QWidget(self.HomeMain)
        self.progressGame.setObjectName(u"progressGame")
        self.progressGame.setMinimumSize(QSize(0, 10))
        self.verticalLayout_12 = QVBoxLayout(self.progressGame)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.GameName = QLabel(self.progressGame)
        self.GameName.setObjectName(u"GameName")

        self.verticalLayout_12.addWidget(self.GameName)

        self.Searchprogress = QProgressBar(self.progressGame)
        self.Searchprogress.setObjectName(u"Searchprogress")
        self.Searchprogress.setValue(24)

        self.verticalLayout_12.addWidget(self.Searchprogress)


        self.verticalLayout_7.addWidget(self.progressGame)

        self.mainBodyContent = QWidget(self.HomeMain)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy)
        self.mainBodyContent.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_5 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.mainBodyContent)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setEnabled(True)
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy6)
        self.widget_3.setMinimumSize(QSize(500, 0))
        self.widget_3.setSizeIncrement(QSize(0, 0))
        self.verticalLayout_11 = QVBoxLayout(self.widget_3)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(9, 9, 9, 9)
        self.widget_7 = QWidget(self.widget_3)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_19 = QVBoxLayout(self.widget_7)
        self.verticalLayout_19.setSpacing(6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(9, 9, 9, 20)
        self.OS = QLabel(self.widget_7)
        self.OS.setObjectName(u"OS")

        self.verticalLayout_19.addWidget(self.OS)


        self.verticalLayout_11.addWidget(self.widget_7)

        self.widget_11 = QWidget(self.widget_3)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_17 = QVBoxLayout(self.widget_11)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, -1, -1, 20)
        self.RAM = QLabel(self.widget_11)
        self.RAM.setObjectName(u"RAM")

        self.verticalLayout_17.addWidget(self.RAM)


        self.verticalLayout_11.addWidget(self.widget_11)

        self.widget_10 = QWidget(self.widget_3)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_16 = QVBoxLayout(self.widget_10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, -1, -1, 20)
        self.CPU = QLabel(self.widget_10)
        self.CPU.setObjectName(u"CPU")

        self.verticalLayout_16.addWidget(self.CPU)


        self.verticalLayout_11.addWidget(self.widget_10)

        self.widget_9 = QWidget(self.widget_3)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_21 = QVBoxLayout(self.widget_9)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, -1, -1, 20)
        self.GPU = QLabel(self.widget_9)
        self.GPU.setObjectName(u"GPU")

        self.verticalLayout_21.addWidget(self.GPU)


        self.verticalLayout_11.addWidget(self.widget_9)

        self.widget_8 = QWidget(self.widget_3)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_20 = QVBoxLayout(self.widget_8)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(-1, -1, -1, 20)
        self.DIskUsage = QLabel(self.widget_8)
        self.DIskUsage.setObjectName(u"DIskUsage")

        self.verticalLayout_20.addWidget(self.DIskUsage)


        self.verticalLayout_11.addWidget(self.widget_8)


        self.horizontalLayout_5.addWidget(self.widget_3)

        self.widget_6 = QWidget(self.mainBodyContent)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_13 = QVBoxLayout(self.widget_6)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.widget_6)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pushButton_6 = QPushButton(self.widget_12)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCheckable(False)

        self.horizontalLayout_13.addWidget(self.pushButton_6)


        self.verticalLayout_13.addWidget(self.widget_12)

        self.widget_13 = QWidget(self.widget_6)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pushButton_7 = QPushButton(self.widget_13)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_14.addWidget(self.pushButton_7)


        self.verticalLayout_13.addWidget(self.widget_13)

        self.widget_14 = QWidget(self.widget_6)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.pushButton_8 = QPushButton(self.widget_14)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_15.addWidget(self.pushButton_8)


        self.verticalLayout_13.addWidget(self.widget_14)

        self.widget_17 = QWidget(self.widget_6)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.pushButton_9 = QPushButton(self.widget_17)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_17.addWidget(self.pushButton_9)


        self.verticalLayout_13.addWidget(self.widget_17)

        self.widget_16 = QWidget(self.widget_6)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.pushButton_10 = QPushButton(self.widget_16)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_16.addWidget(self.pushButton_10)


        self.verticalLayout_13.addWidget(self.widget_16)


        self.horizontalLayout_5.addWidget(self.widget_6)


        self.verticalLayout_7.addWidget(self.mainBodyContent)

        self.searchBarspace = QSpacerItem(10, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_7.addItem(self.searchBarspace)

        self.State = QWidget(self.HomeMain)
        self.State.setObjectName(u"State")
        self.State.setEnabled(True)
        self.State.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.State)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.State)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.State)

        self.stackedWidget_2.addWidget(self.HomeMain)
        self.InformationMain = QWidget()
        self.InformationMain.setObjectName(u"InformationMain")
        self.horizontalLayout_6 = QHBoxLayout(self.InformationMain)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_5 = QWidget(self.InformationMain)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_14 = QVBoxLayout(self.widget_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_14.addWidget(self.label_5)

        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_14.addWidget(self.label_6)

        self.label_7 = QLabel(self.widget_5)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_14.addWidget(self.label_7)

        self.label_8 = QLabel(self.widget_5)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_14.addWidget(self.label_8)

        self.label_9 = QLabel(self.widget_5)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_14.addWidget(self.label_9)

        self.label_10 = QLabel(self.widget_5)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_14.addWidget(self.label_10)


        self.horizontalLayout_6.addWidget(self.widget_5)

        self.stackedWidget_2.addWidget(self.InformationMain)

        self.horizontalLayout_8.addWidget(self.stackedWidget_2)


        self.verticalLayout_10.addWidget(self.widget_2)


        self.horizontalLayout.addWidget(self.MainBodyContainer)

        dashboard.setCentralWidget(self.centralwidget)

        self.retranslateUi(dashboard)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(dashboard)
    # setupUi

    def retranslateUi(self, dashboard):
        dashboard.setWindowTitle(QCoreApplication.translate("dashboard", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.MenuButton.setToolTip(QCoreApplication.translate("dashboard", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.MenuButton.setText("")
#if QT_CONFIG(tooltip)
        self.Homebutton.setToolTip(QCoreApplication.translate("dashboard", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.Homebutton.setText(QCoreApplication.translate("dashboard", u"Home", None))
#if QT_CONFIG(tooltip)
        self.SettingsButton.setToolTip(QCoreApplication.translate("dashboard", u"Go to Settings", None))
#endif // QT_CONFIG(tooltip)
        self.SettingsButton.setText(QCoreApplication.translate("dashboard", u"Past Searches", None))
#if QT_CONFIG(tooltip)
        self.InfoButton.setToolTip(QCoreApplication.translate("dashboard", u"Access to more Information", None))
#endif // QT_CONFIG(tooltip)
        self.InfoButton.setText(QCoreApplication.translate("dashboard", u"Information", None))
#if QT_CONFIG(tooltip)
        self.LogoutButton.setToolTip(QCoreApplication.translate("dashboard", u"For logging Out", None))
#endif // QT_CONFIG(tooltip)
        self.LogoutButton.setText(QCoreApplication.translate("dashboard", u"Logout", None))
        self.label_2.setText(QCoreApplication.translate("dashboard", u"More Menu", None))
        self.pushButton_2.setText("")
        self.PastSearches.setText(QCoreApplication.translate("dashboard", u"PastSearches", None))
        self.Information.setText(QCoreApplication.translate("dashboard", u"Information", None))
        self.label.setText(QCoreApplication.translate("dashboard", u"AppName", None))
        self.Minimize_window.setText("")
        self.Maximize_window.setText("")
        self.Close_window.setText("")
        self.pushButton.setText("")
        self.GameName.setText(QCoreApplication.translate("dashboard", u"GAME NAME", None))
        self.OS.setText(QCoreApplication.translate("dashboard", u"Operating System", None))
        self.RAM.setText(QCoreApplication.translate("dashboard", u"RAM", None))
        self.CPU.setText(QCoreApplication.translate("dashboard", u"CPU", None))
        self.GPU.setText(QCoreApplication.translate("dashboard", u"GPU", None))
        self.DIskUsage.setText(QCoreApplication.translate("dashboard", u"Disk Usage", None))
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.pushButton_8.setText("")
        self.pushButton_9.setText("")
        self.pushButton_10.setText("")
        self.label_3.setText(QCoreApplication.translate("dashboard", u"Compatiblity Status", None))
        self.label_4.setText(QCoreApplication.translate("dashboard", u"System Details", None))
        self.label_5.setText(QCoreApplication.translate("dashboard", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("dashboard", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("dashboard", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("dashboard", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("dashboard", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("dashboard", u"TextLabel", None))
    # retranslateUi

