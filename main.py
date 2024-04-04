
#IMPORTS

import sys
import os

# IMPORT GUI FILE
from src.ui_login_interface import *



# IMPORT Custom widgets
from Custom_Widgets import *

from Custom_Widgets.QAppSettings import QAppSettings


#MAIN WINDOW CLASS

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # APPLY JSON STYLESHEET

        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui,jsonFiles={
            "json-files/login_style.json"
        })
        QAppSettings.updateAppSettings(self )
        self.show()

        #event listeners
        self.ui.login_button.clicked.connect(lambda: self.showNotif("Login Button Clicked!!"))
        self.ui.register_button.clicked.connect(lambda: self.showNotif("Register Button Clicked!!"))

        #change theme
        self.ui.checkBox_2.stateChanged.connect(lambda: self.ChangeTheme())

    #function to display notification:
    def showNotif(self, msg):
            self.ui.notification_txt.setText(msg)
            self.ui.notification_slide.expandMenu()
    #function to switch menu
    def ChangeTheme(self):
        settings = QSettings()
        print("Current theme", settings.value("THEME"))

        if settings.value("THEME") == "Modern Teal Slate":
            settings.setValue("THEME", "Midnight Teal Slate")

            style = " #stackedWidget *{color: #f0f0f0;background-color: transparent;}"
            style2 = """QPushButton{
                     color: #f0f0f0;
                }"""
        else:
            settings.setValue("THEME", "Modern Teal Slate")

            style = "#stackedWidget *{color: #f5f5f5;background-color: transparent;}"
            style2 = """ #frame_4 QPushButton{
                    color: #f5f5f5;
                    }"""
        QAppSettings.updateAppSettings(self)

        self.ui.stackedWidget.setStyleSheet(style)
        self.ui.frame_4.setStyleSheet(style2)
        self.ui.frame_8.setStyleSheet(style2    )
#EXECUTE APP

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

#END===>

