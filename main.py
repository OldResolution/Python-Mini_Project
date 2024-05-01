# IMPORTS
import sys
import os
from PySide6 import *
from PySide6.QtCore import *
# IMPORT GUI FILE
from src.ui_login_interface import *
from src.ui_dashboard import *
from database import login, signup_user  # Import login and signup_user functions from database module

# IMPORT Custom widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings


# MAIN WINDOW CLASS
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_login()
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
    # Modify the login function in the MainWindow class
    def login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if not username and not password:
            self.showNotif("Username and password are empty")
        elif not username:
            self.showNotif("Username is empty")
        elif not password:
            self.showNotif("Password is empty")
        else:
            success, message = login(username, password)
            if success:
                self.hide()  # Hide the login window
                self.dashboard = DashboardWindow()  # Create an instance of the dashboard window
                self.dashboard.show()  # Show the dashboard window
            else:
                self.showNotif(message)

    # Function to handle signup
    def signup(self):
        username = self.ui.r_username.text()
        password = self.ui.r_password.text()
        confirm_password = self.ui.r_conpasswprd.text()
        email = self.ui.r_emailid.text()

        if not (username or password or confirm_password or email):
            self.showNotif("All fields are empty")
        elif not username:
            self.showNotif("Username is empty")
        elif not password:
            self.showNotif("Password is empty")
        elif not confirm_password:
            self.showNotif("Confirm password is empty")
        elif not email:
            self.showNotif("Email is empty")
        elif password != confirm_password:
            self.showNotif("Passwords do not match")
        else:
            success, message = signup_user(username, password, email)
            self.showNotif(message)

class DashboardWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_dashboard()
        self.ui.setupUi(self)

        loadJsonStyle(self, self.ui, jsonFiles={"json-files/dashboard_style.json"})
        QAppSettings.updateAppSettings(self)
        self.show()

        #expand central menu widget  size
        self.ui.past_searches.clicked.connect(lambda: self.ui.CenterMenuContainer.expandMenu())
        self.ui.InfoButton.clicked.connect(lambda: self.ui.CenterMenuContainer.expandMenu())

        #close central menu widget
        self.ui.Close_menu.clicked.connect(lambda: self.ui.CenterMenuContainer.collapseMenu())

        #logout
        self.ui.LogoutButton.clicked.connect(self.logout)

    def logout(self):
        self.hide()  # Hide the login window
        self.logout = MainWindow()  # Create an instance of the dashboard window
        self.logout.show()  # Show the dashboard window

   # def Comparison_menu(self):

   # def System_info(self):

# EXECUTE APP
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DashboardWindow()
    sys.exit(app.exec_())
