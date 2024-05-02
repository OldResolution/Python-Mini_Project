# IMPORTS
import sys
import os

from PySide6 import *
from PySide6.QtCore import *
# IMPORT GUI FILE
from src.ui_login_interface import *
from src.ui_dashboard import *
from database import login, signup_user  # Import login and signup_user functions from database module
from comparison_operator import Compare_minimum_info
from system_info import Get_User_Info
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

from PySide6.QtWidgets import QLabel

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
        #dashboard buttons
        self.ui.searchButton.clicked.connect(self.Comparison_menu)
        self.ui.InfoButton.clicked.connect(self.System_info)
        self.ui.searchButton.clicked.connect(self.handle_search)
        self.history_label = self.ui.pastSearches
        self.search_history = []

    def logout(self):
        self.hide()  # Hide the login window
        self.logout = MainWindow()  # Create an instance of the dashboard window
        self.logout.show()  # Show the dashboard window

    def Comparison_menu(self):
        gamename = self.ui.searchBar.text()

        # Set the game name label
        self.ui.GameName.setText(gamename)

        compatibility = Compare_minimum_info(gamename)

        # Map compatibility status to icon paths
        icon_status_map = {
            "Compatible": "Qss/icons/333333/feather/check-square.png",
            "Incompatible": "Qss/icons/333333/feather/x-square.png",
        }

        # Update buttons based on compatibility status
        button_map = {
            "OS": self.ui.Os_button,
            "RAM": self.ui.Ram_button,
            "CPU": self.ui.Cpu_button,
            "GPU": self.ui.Gpu_button,
            "ROM": self.ui.Disk_button,
        }

        for component, status in compatibility.items():
            button = button_map.get(component)
            if button:
                icon_path = icon_status_map.get(status, "")
                if icon_path:
                    icon = QIcon(icon_path)
                    button.setIcon(icon)
                    button.setIconSize(QSize(20, 20))  # Adjust icon size as needed
            else:
                print(f"No button found for component: {component}")

    def System_info(self):
        os, processor, ram, rom, gpu = Get_User_Info()

        # Set the text of labels with the obtained user information
        self.ui.OS_Info.setText(f"Operating System:"+os)
        self.ui.CPU_info.setText(f"CPU:"+processor)
        self.ui.RAM_info.setText(f"RAM:"+ram)
        self.ui.Disk_Usage_Info.setText(f"ROM:"+rom)
        self.ui.GPU_info.setText(f"GPU:"+gpu)

    def handle_search(self):
        game_name = self.ui.searchBar.text()
        if game_name:  # Ensure non-empty string
            self.search_history.append(game_name)  # Add game name to history
            print("Search history:", self.search_history)  # Print search history for debugging
            self.update_history_label()

    def update_history_label(self):
        history_text = "\n".join(self.search_history)  # Concatenate search history with newline separator
        self.history_label.setText(history_text)  # Set the text of the label to the concatenated search history


# EXECUTE APP
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DashboardWindow()
    sys.exit(app.exec_())
