# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_forgot_password.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 299)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.notification_fg = QLabel(self.frame_2)
        self.notification_fg.setObjectName(u"notification_fg")

        self.horizontalLayout.addWidget(self.notification_fg)


        self.verticalLayout.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ForgotPassword4 = QLabel(self.frame)
        self.ForgotPassword4.setObjectName(u"ForgotPassword4")

        self.verticalLayout_2.addWidget(self.ForgotPassword4, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.Username = QLineEdit(self.frame)
        self.Username.setObjectName(u"Username")

        self.verticalLayout_2.addWidget(self.Username, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.NewPassword = QLineEdit(self.frame)
        self.NewPassword.setObjectName(u"NewPassword")
        self.NewPassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.NewPassword, 0, Qt.AlignHCenter)

        self.RENewPassword = QLineEdit(self.frame)
        self.RENewPassword.setObjectName(u"RENewPassword")

        self.verticalLayout_2.addWidget(self.RENewPassword, 0, Qt.AlignHCenter)

        self.Confirm = QPushButton(self.frame)
        self.Confirm.setObjectName(u"Confirm")

        self.verticalLayout_2.addWidget(self.Confirm, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.notification_fg.setText("")
#if QT_CONFIG(whatsthis)
        self.ForgotPassword4.setWhatsThis(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Forgot Password</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.ForgotPassword4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Forgot Password</span></p></body></html>", None))
        self.Username.setInputMask("")
        self.Username.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.NewPassword.setPlaceholderText(QCoreApplication.translate("Form", u"New Password", None))
        self.RENewPassword.setPlaceholderText(QCoreApplication.translate("Form", u"Retype New Password", None))
        self.Confirm.setText(QCoreApplication.translate("Form", u"Confirm", None))
    # retranslateUi

