# IMPORTS
import sys
import os

# IMPORT GUI FILE
from src.ui_login_interface import *
from database import login, signup_user  # Import login and signup_user functions from database module

# IMPORT Custom widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings

# MAIN WINDOW CLASS
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # APPLY JSON STYLESHEET

        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui, jsonFiles={"json-files/login_style.json"})
        QAppSettings.updateAppSettings(self)
        self.show()

        # Connect login and signup functions to buttons
        self.ui.login_button.clicked.connect(self.login)
        self.ui.register_button.clicked.connect(self.signup)

    # Function to display notification
    def showNotif(self, msg):
        self.ui.notification_txt.setText(msg)
        self.ui.notification_slide.expandMenu()

    # Function to handle login
    def login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        success, message = login(username, password)
        self.showNotif(message)

    # Function to handle signup
    def signup(self):
        if self.ui.r_password.text() == self.ui.r_conpasswprd.text():
            username = self.ui.r_username.text()
            password = self.ui.r_password.text()
            email = self.ui.r_emailid.text()
            success, message = signup_user(username, password, email)
            self.showNotif(message)
        else:
            self.showNotif("Passwords do not match")

# EXECUTE APP
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
