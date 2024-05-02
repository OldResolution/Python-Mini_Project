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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
class Ui_dashboard(object):
    def setupUi(self, dashboard):
        if not dashboard.objectName():
            dashboard.setObjectName(u"dashboard")
        dashboard.resize(850, 598)
        dashboard.setStyleSheet(u"")
        self.dash_centralwidget = QWidget(dashboard)
        self.dash_centralwidget.setObjectName(u"dash_centralwidget")
        self.horizontalLayout = QHBoxLayout(self.dash_centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuContainer = QCustomSlideMenu(self.dash_centralwidget)
        self.LeftMenuContainer.setObjectName(u"LeftMenuContainer")
        self.LeftMenuContainer.setMaximumSize(QSize(35, 16777215))
        self.LeftMenuContainer.setStyleSheet(u"QPushButton{\n"
"text-align:left;\n"
"padding:4 px 5 px;\n"
"}")
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
        self.Homebutton.setMaximumSize(QSize(16777215, 16777215))
        self.Homebutton.setAutoFillBackground(False)
        self.Homebutton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/feather/icons/feather/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Homebutton.setIcon(icon1)
        self.Homebutton.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.Homebutton)

        self.past_searches = QPushButton(self.frame_2)
        self.past_searches.setObjectName(u"past_searches")
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/chevrons-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.past_searches.setIcon(icon2)
        self.past_searches.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.past_searches)


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
        font = QFont()
        font.setBold(False)
        self.LogoutButton.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/material_design/icons/material_design/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.LogoutButton.setIcon(icon4)
        self.LogoutButton.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.LogoutButton)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.LeftMenuSubContainer)


        self.horizontalLayout.addWidget(self.LeftMenuContainer)

        self.CenterMenuContainer = QCustomSlideMenu(self.dash_centralwidget)
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
        self.More_menu_Frame = QFrame(self.CenterMenuSubContainer)
        self.More_menu_Frame.setObjectName(u"More_menu_Frame")
        self.More_menu_Frame.setFrameShape(QFrame.StyledPanel)
        self.More_menu_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.More_menu_Frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.More_menu = QLabel(self.More_menu_Frame)
        self.More_menu.setObjectName(u"More_menu")
        self.More_menu.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.More_menu)

        self.Close_menu = QPushButton(self.More_menu_Frame)
        self.Close_menu.setObjectName(u"Close_menu")
        self.Close_menu.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/feather/icons/feather/x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Close_menu.setIcon(icon5)
        self.Close_menu.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.Close_menu, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.More_menu_Frame, 0, Qt.AlignRight|Qt.AlignTop)

        self.Side_Bar = QCustomQStackedWidget(self.CenterMenuSubContainer)
        self.Side_Bar.setObjectName(u"Side_Bar")
        self.Side_Bar.setLineWidth(0)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pastSearches = QLabel(self.page_2)
        self.pastSearches.setObjectName(u"pastSearches")

        self.verticalLayout_8.addWidget(self.pastSearches)

        self.Side_Bar.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.page_3.sizePolicy().hasHeightForWidth())
        self.page_3.setSizePolicy(sizePolicy2)
        self.verticalLayout_9 = QVBoxLayout(self.page_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.Information = QLabel(self.page_3)
        self.Information.setObjectName(u"Information")
        font1 = QFont()
        font1.setPointSize(13)
        self.Information.setFont(font1)
        self.Information.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.Information)

        self.Side_Bar.addWidget(self.page_3)

        self.verticalLayout_6.addWidget(self.Side_Bar)


        self.verticalLayout_5.addWidget(self.CenterMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.CenterMenuContainer)

        self.MainBodyContainer = QWidget(self.dash_centralwidget)
        self.MainBodyContainer.setObjectName(u"MainBodyContainer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.MainBodyContainer.sizePolicy().hasHeightForWidth())
        self.MainBodyContainer.setSizePolicy(sizePolicy3)
        self.MainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.MainBodyContainer)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_2 = QWidget(self.MainBodyContainer)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.Pages = QCustomQStackedWidget(self.widget_2)
        self.Pages.setObjectName(u"Pages")
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
        self.frame_6.setMinimumSize(QSize(300, 0))
        self.frame_6.setSizeIncrement(QSize(0, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.searchBar = QLineEdit(self.frame_6)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.searchBar.sizePolicy().hasHeightForWidth())
        self.searchBar.setSizePolicy(sizePolicy4)
        self.searchBar.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_10.addWidget(self.searchBar)

        self.searchButton = QPushButton(self.frame_6)
        self.searchButton.setObjectName(u"searchButton")
        sizePolicy4.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy4)
        icon6 = QIcon()
        icon6.addFile(u":/feather/icons/feather/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon6)

        self.horizontalLayout_10.addWidget(self.searchButton)


        self.horizontalLayout_9.addWidget(self.frame_6)


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
        font2 = QFont()
        font2.setHintingPreference(QFont.PreferDefaultHinting)
        self.GameName.setFont(font2)

        self.verticalLayout_12.addWidget(self.GameName)

        self.Searchprogress = QProgressBar(self.progressGame)
        self.Searchprogress.setObjectName(u"Searchprogress")
        sizePolicy4.setHeightForWidth(self.Searchprogress.sizePolicy().hasHeightForWidth())
        self.Searchprogress.setSizePolicy(sizePolicy4)
        self.Searchprogress.setValue(24)

        self.verticalLayout_12.addWidget(self.Searchprogress)


        self.verticalLayout_7.addWidget(self.progressGame)

        self.mainBodyContent = QWidget(self.HomeMain)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy)
        self.mainBodyContent.setMinimumSize(QSize(0, 40))
        self.mainBodyContent.setStyleSheet(u"#GPU_tick,#Os_tick,#Ram_tick,#cpu_tick,#disk_tick {\n"
"  border: 2px;\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.mainBodyContent)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy2)
        self.widget_3.setMinimumSize(QSize(580, 0))
        self.widget_3.setSizeIncrement(QSize(0, 0))
        self.verticalLayout_11 = QVBoxLayout(self.widget_3)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(9, 9, 20, 9)
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

        self.divide1 = QFrame(self.widget_3)
        self.divide1.setObjectName(u"divide1")
        self.divide1.setMinimumSize(QSize(625, 0))
        self.divide1.setFrameShape(QFrame.HLine)
        self.divide1.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.divide1)

        self.widget_11 = QWidget(self.widget_3)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_17 = QVBoxLayout(self.widget_11)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, -1, -1, 20)
        self.RAM = QLabel(self.widget_11)
        self.RAM.setObjectName(u"RAM")

        self.verticalLayout_17.addWidget(self.RAM)


        self.verticalLayout_11.addWidget(self.widget_11)

        self.divide2 = QFrame(self.widget_3)
        self.divide2.setObjectName(u"divide2")
        self.divide2.setMinimumSize(QSize(625, 0))
        self.divide2.setFrameShape(QFrame.HLine)
        self.divide2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.divide2)

        self.widget_10 = QWidget(self.widget_3)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_16 = QVBoxLayout(self.widget_10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, -1, -1, 20)
        self.CPU = QLabel(self.widget_10)
        self.CPU.setObjectName(u"CPU")

        self.verticalLayout_16.addWidget(self.CPU)


        self.verticalLayout_11.addWidget(self.widget_10)

        self.divide3 = QFrame(self.widget_3)
        self.divide3.setObjectName(u"divide3")
        self.divide3.setMinimumSize(QSize(625, 0))
        self.divide3.setFrameShape(QFrame.HLine)
        self.divide3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.divide3)

        self.widget_9 = QWidget(self.widget_3)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_21 = QVBoxLayout(self.widget_9)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, -1, -1, 20)
        self.GPU = QLabel(self.widget_9)
        self.GPU.setObjectName(u"GPU")

        self.verticalLayout_21.addWidget(self.GPU)


        self.verticalLayout_11.addWidget(self.widget_9)

        self.divide4 = QFrame(self.widget_3)
        self.divide4.setObjectName(u"divide4")
        self.divide4.setMinimumSize(QSize(625, 0))
        self.divide4.setFrameShape(QFrame.HLine)
        self.divide4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.divide4)

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
        self.widget_6.setStyleSheet(u"#widget_6 *{\n"
"  bor;\n"
"}")
        self.verticalLayout_13 = QVBoxLayout(self.widget_6)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.Os_tick = QWidget(self.widget_6)
        self.Os_tick.setObjectName(u"Os_tick")
        self.Os_tick.setStyleSheet(u"")
        self.horizontalLayout_13 = QHBoxLayout(self.Os_tick)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.Os_button = QPushButton(self.Os_tick)
        self.Os_button.setObjectName(u"Os_button")
        sizePolicy.setHeightForWidth(self.Os_button.sizePolicy().hasHeightForWidth())
        self.Os_button.setSizePolicy(sizePolicy)
        self.Os_button.setStyleSheet(u"")
        self.Os_button.setCheckable(False)

        self.horizontalLayout_13.addWidget(self.Os_button, 0, Qt.AlignRight)


        self.verticalLayout_13.addWidget(self.Os_tick)

        self.Ram_tick = QWidget(self.widget_6)
        self.Ram_tick.setObjectName(u"Ram_tick")
        self.horizontalLayout_14 = QHBoxLayout(self.Ram_tick)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.Ram_button = QPushButton(self.Ram_tick)
        self.Ram_button.setObjectName(u"Ram_button")
        sizePolicy.setHeightForWidth(self.Ram_button.sizePolicy().hasHeightForWidth())
        self.Ram_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.Ram_button, 0, Qt.AlignRight)


        self.verticalLayout_13.addWidget(self.Ram_tick)

        self.cpu_tick = QWidget(self.widget_6)
        self.cpu_tick.setObjectName(u"cpu_tick")
        self.horizontalLayout_15 = QHBoxLayout(self.cpu_tick)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.Cpu_button = QPushButton(self.cpu_tick)
        self.Cpu_button.setObjectName(u"Cpu_button")
        sizePolicy.setHeightForWidth(self.Cpu_button.sizePolicy().hasHeightForWidth())
        self.Cpu_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_15.addWidget(self.Cpu_button)


        self.verticalLayout_13.addWidget(self.cpu_tick, 0, Qt.AlignRight)

        self.GPU_tick = QWidget(self.widget_6)
        self.GPU_tick.setObjectName(u"GPU_tick")
        self.horizontalLayout_17 = QHBoxLayout(self.GPU_tick)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, -1, -1, -1)
        self.Gpu_button = QPushButton(self.GPU_tick)
        self.Gpu_button.setObjectName(u"Gpu_button")
        sizePolicy.setHeightForWidth(self.Gpu_button.sizePolicy().hasHeightForWidth())
        self.Gpu_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_17.addWidget(self.Gpu_button, 0, Qt.AlignRight)


        self.verticalLayout_13.addWidget(self.GPU_tick)

        self.disk_tick_2 = QWidget(self.widget_6)
        self.disk_tick_2.setObjectName(u"disk_tick_2")
        self.horizontalLayout_16 = QHBoxLayout(self.disk_tick_2)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, -1, -1, -1)
        self.Disk_button = QPushButton(self.disk_tick_2)
        self.Disk_button.setObjectName(u"Disk_button")
        sizePolicy.setHeightForWidth(self.Disk_button.sizePolicy().hasHeightForWidth())
        self.Disk_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_16.addWidget(self.Disk_button, 0, Qt.AlignRight)


        self.verticalLayout_13.addWidget(self.disk_tick_2)


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
        self.Compatiblity_status = QLabel(self.State)
        self.Compatiblity_status.setObjectName(u"Compatiblity_status")

        self.horizontalLayout_3.addWidget(self.Compatiblity_status, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.State)

        self.Pages.addWidget(self.HomeMain)
        self.InformationMain = QWidget()
        self.InformationMain.setObjectName(u"InformationMain")
        self.InformationMain.setStyleSheet(u"#InformationMain QLabel{\n"
"  font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;\n"
"}\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(self.InformationMain)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_5 = QWidget(self.InformationMain)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_14 = QVBoxLayout(self.widget_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.Title_System = QLabel(self.widget_5)
        self.Title_System.setObjectName(u"Title_System")
        self.Title_System.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.Title_System)

        self.OS_Info = QLabel(self.widget_5)
        self.OS_Info.setObjectName(u"OS_Info")

        self.verticalLayout_14.addWidget(self.OS_Info)

        self.RAM_info = QLabel(self.widget_5)
        self.RAM_info.setObjectName(u"RAM_info")

        self.verticalLayout_14.addWidget(self.RAM_info)

        self.CPU_info = QLabel(self.widget_5)
        self.CPU_info.setObjectName(u"CPU_info")

        self.verticalLayout_14.addWidget(self.CPU_info)

        self.GPU_info = QLabel(self.widget_5)
        self.GPU_info.setObjectName(u"GPU_info")

        self.verticalLayout_14.addWidget(self.GPU_info)

        self.Disk_Usage_Info = QLabel(self.widget_5)
        self.Disk_Usage_Info.setObjectName(u"Disk_Usage_Info")

        self.verticalLayout_14.addWidget(self.Disk_Usage_Info)


        self.horizontalLayout_6.addWidget(self.widget_5)

        self.Pages.addWidget(self.InformationMain)

        self.horizontalLayout_8.addWidget(self.Pages)


        self.verticalLayout_10.addWidget(self.widget_2)


        self.horizontalLayout.addWidget(self.MainBodyContainer)

        dashboard.setCentralWidget(self.dash_centralwidget)

        self.retranslateUi(dashboard)

        self.Side_Bar.setCurrentIndex(1)
        self.Pages.setCurrentIndex(0)


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
        self.past_searches.setToolTip(QCoreApplication.translate("dashboard", u"Go to Settings", None))
#endif // QT_CONFIG(tooltip)
        self.past_searches.setText(QCoreApplication.translate("dashboard", u"Past Searches", None))
#if QT_CONFIG(tooltip)
        self.InfoButton.setToolTip(QCoreApplication.translate("dashboard", u"Access to more Information", None))
#endif // QT_CONFIG(tooltip)
        self.InfoButton.setText(QCoreApplication.translate("dashboard", u"Information", None))
#if QT_CONFIG(tooltip)
        self.LogoutButton.setToolTip(QCoreApplication.translate("dashboard", u"For logging Out", None))
#endif // QT_CONFIG(tooltip)
        self.LogoutButton.setText(QCoreApplication.translate("dashboard", u"Logout", None))
        self.More_menu.setText(QCoreApplication.translate("dashboard", u"More Menu", None))
        self.Close_menu.setText("")
        self.pastSearches.setText("")
        self.Information.setText("")
        self.searchButton.setText(QCoreApplication.translate("dashboard", u"Search", None))
        self.GameName.setText("")
        self.OS.setText(QCoreApplication.translate("dashboard", u"Operating System", None))
        self.RAM.setText(QCoreApplication.translate("dashboard", u"RAM", None))
        self.CPU.setText(QCoreApplication.translate("dashboard", u"CPU", None))
        self.GPU.setText(QCoreApplication.translate("dashboard", u"GPU", None))
        self.DIskUsage.setText(QCoreApplication.translate("dashboard", u"Disk Usage", None))
        self.Os_button.setText("")
        self.Ram_button.setText("")
        self.Cpu_button.setText("")
        self.Gpu_button.setText("")
        self.Disk_button.setText("")
        self.Compatiblity_status.setText("")
#if QT_CONFIG(whatsthis)
        self.Title_System.setWhatsThis(QCoreApplication.translate("dashboard", u"<html><head/><body><p align=\"center\">System Details</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Title_System.setText(QCoreApplication.translate("dashboard", u"System Details", None))
        self.OS_Info.setText("")
        self.RAM_info.setText("")
        self.CPU_info.setText("")
        self.GPU_info.setText("")
        self.Disk_Usage_Info.setText("")
    # retranslateUi

