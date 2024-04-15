
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


    #function to display notification:
    def showNotif(self, msg):
            self.ui.notification_txt.setText(msg)
            self.ui.notification_slide.expandMenu()

#EXECUTE APP

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

#END===>

