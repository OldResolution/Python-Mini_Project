# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_login_interface.ui'
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

from Custom_Widgets.QCustomCheckBox import QCustomCheckBox
from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(658, 411)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setCursor(QCursor(Qt.ArrowCursor))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 5, 0, 25)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 5, 5, 0)
        self.notification_slide = QCustomSlideMenu(self.header)
        self.notification_slide.setObjectName(u"notification_slide")
        self.notification_slide.setMinimumSize(QSize(600, 0))
        self.notification_slide.setMaximumSize(QSize(600, 16777215))
        self.horizontalLayout_6 = QHBoxLayout(self.notification_slide)
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.notification_slide)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(234, 38))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.notification_txt = QLabel(self.frame_9)
        self.notification_txt.setObjectName(u"notification_txt")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notification_txt.sizePolicy().hasHeightForWidth())
        self.notification_txt.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        self.notification_txt.setFont(font)
        self.notification_txt.setAlignment(Qt.AlignCenter)
        self.notification_txt.setWordWrap(False)

        self.horizontalLayout_7.addWidget(self.notification_txt)


        self.horizontalLayout_6.addWidget(self.frame_9, 0, Qt.AlignHCenter)

        self.close_notification = QPushButton(self.notification_slide)
        self.close_notification.setObjectName(u"close_notification")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.close_notification.sizePolicy().hasHeightForWidth())
        self.close_notification.setSizePolicy(sizePolicy1)
        self.close_notification.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_notification.setIcon(icon)

        self.horizontalLayout_6.addWidget(self.close_notification, 0, Qt.AlignRight)


        self.horizontalLayout_2.addWidget(self.notification_slide)

        self.close_window_button = QPushButton(self.header)
        self.close_window_button.setObjectName(u"close_window_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.close_window_button.sizePolicy().hasHeightForWidth())
        self.close_window_button.setSizePolicy(sizePolicy2)
        self.close_window_button.setMinimumSize(QSize(0, 0))
        self.close_window_button.setMaximumSize(QSize(24, 24))
        self.close_window_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_window_button.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u":/feather/icons/feather/x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.close_window_button, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.header)

        self.main_body = QWidget(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setCursor(QCursor(Qt.PointingHandCursor))
        self.main_body.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.main_body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QCustomQStackedWidget(self.main_body)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.welcome_login_pg = QWidget()
        self.welcome_login_pg.setObjectName(u"welcome_login_pg")
        self.welcome_login_pg.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.welcome_login_pg)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.welcome_login_pg)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.to_signup = QPushButton(self.frame)
        self.to_signup.setObjectName(u"to_signup")
        self.to_signup.setMinimumSize(QSize(0, 0))
        self.to_signup.setFont(font)
        self.to_signup.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.to_signup, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.welcome_login_pg)
        self.welcome_signup_pg = QWidget()
        self.welcome_signup_pg.setObjectName(u"welcome_signup_pg")
        self.verticalLayout_8 = QVBoxLayout(self.welcome_signup_pg)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_5 = QFrame(self.welcome_signup_pg)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(9, 9, 9, 9)
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_7.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_9)

        self.to_login = QPushButton(self.frame_5)
        self.to_login.setObjectName(u"to_login")
        self.to_login.setFont(font)
        self.to_login.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.to_login, 0, Qt.AlignHCenter)


        self.verticalLayout_8.addWidget(self.frame_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.welcome_signup_pg)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.stackedWidget_2 = QCustomQStackedWidget(self.main_body)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.login_pg = QWidget()
        self.login_pg.setObjectName(u"login_pg")
        self.verticalLayout_4 = QVBoxLayout(self.login_pg)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.login_pg)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(200, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(200, 0))
        self.lineEdit.setFont(font)

        self.verticalLayout_5.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(200, 0))
        self.lineEdit_2.setFont(font)

        self.verticalLayout_5.addWidget(self.lineEdit_2)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setOpenExternalLinks(True)

        self.verticalLayout_5.addWidget(self.label_5)

        self.login_button = QPushButton(self.frame_3)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setFont(font)
        self.login_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.login_button)


        self.verticalLayout_6.addWidget(self.frame_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_6)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.google = QPushButton(self.frame_4)
        self.google.setObjectName(u"google")
        self.google.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/font_awesome_brands/icons/font_awesome/brands/google-plus-g.png", QSize(), QIcon.Normal, QIcon.Off)
        self.google.setIcon(icon2)
        self.google.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.google)

        self.github = QPushButton(self.frame_4)
        self.github.setObjectName(u"github")
        self.github.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/font_awesome_brands/icons/font_awesome/brands/github.png", QSize(), QIcon.Normal, QIcon.Off)
        self.github.setIcon(icon3)
        self.github.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.github)


        self.verticalLayout_6.addWidget(self.frame_4)


        self.verticalLayout_4.addWidget(self.frame_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget_2.addWidget(self.login_pg)
        self.signup_pg = QWidget()
        self.signup_pg.setObjectName(u"signup_pg")
        self.verticalLayout_11 = QVBoxLayout(self.signup_pg)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_6 = QFrame(self.signup_pg)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_9.addWidget(self.label_10)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(200, 0))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.r_username = QLineEdit(self.frame_7)
        self.r_username.setObjectName(u"r_username")
        self.r_username.setMinimumSize(QSize(200, 0))
        self.r_username.setFont(font)

        self.verticalLayout_10.addWidget(self.r_username)

        self.r_password = QLineEdit(self.frame_7)
        self.r_password.setObjectName(u"r_password")
        self.r_password.setFont(font)

        self.verticalLayout_10.addWidget(self.r_password)

        self.r_conpasswprd = QLineEdit(self.frame_7)
        self.r_conpasswprd.setObjectName(u"r_conpasswprd")
        self.r_conpasswprd.setFont(font)

        self.verticalLayout_10.addWidget(self.r_conpasswprd)

        self.r_emailid = QLineEdit(self.frame_7)
        self.r_emailid.setObjectName(u"r_emailid")
        self.r_emailid.setFont(font)

        self.verticalLayout_10.addWidget(self.r_emailid)

        self.register_button = QPushButton(self.frame_7)
        self.register_button.setObjectName(u"register_button")
        self.register_button.setFont(font)
        self.register_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_10.addWidget(self.register_button)


        self.verticalLayout_9.addWidget(self.frame_7, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_12)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.google_2 = QPushButton(self.frame_8)
        self.google_2.setObjectName(u"google_2")
        self.google_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.google_2.setIcon(icon2)
        self.google_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.google_2)

        self.github_2 = QPushButton(self.frame_8)
        self.github_2.setObjectName(u"github_2")
        self.github_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.github_2.setIcon(icon3)
        self.github_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.github_2)


        self.verticalLayout_9.addWidget(self.frame_8)


        self.verticalLayout_11.addWidget(self.frame_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget_2.addWidget(self.signup_pg)

        self.horizontalLayout.addWidget(self.stackedWidget_2)


        self.verticalLayout.addWidget(self.main_body)

        self.footer = QFrame(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(20, 0, 0, 0)
        self.checkBox = QCustomCheckBox(self.footer)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_5.addWidget(self.checkBox, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(accessibility)
        MainWindow.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.notification_txt.setText(QCoreApplication.translate("MainWindow", u"Notification message. Click 'ok' to hide", None))
        self.close_notification.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.close_window_button.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Hi,Welcome!!</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Enter your details to login or login with social media apps", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Not Registered? Click below to register.", None))
        self.to_signup.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Hi,Welcome!!</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Enter your details to register. You can also regsiter using social media apps", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Already Registered? Click below to login.", None))
        self.to_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Sign In</span></p></body></html>", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"google.com\"><span style=\" text-decoration: underline; color:#0000ff;\">Forgot your password?</span></a></p></body></html>", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Or Register with socials", None))
        self.google.setText("")
        self.github.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Sign Up</span></p></body></html>", None))
        self.r_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.r_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.r_conpasswprd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.r_emailid.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email ID", None))
        self.register_button.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Or Register with socials", None))
        self.google_2.setText("")
        self.github_2.setText("")
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Remember me", None))
    # retranslateUi

