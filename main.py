import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from login_ui import Ui_Dialog
from mains_gui import ESP32App  # ← Tama, ito ang working loadcell page mo

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked.connect(self.check_login)

        self.correct_username = "owner"
        self.correct_password = "123123"

    def check_login(self):
        username = self.ui.usernameLineEdit.text()
        password = self.ui.passwordLineEdit.text()

        if username == self.correct_username and password == self.correct_password:
            QMessageBox.information(self, "Success", "Login successful!")
            self.accept()
        else:
            self.ui.feedbackLabel.setText("Invalid username or password")

def main():
    app = QApplication(sys.argv)
    login = LoginDialog()

    if login.exec_() == QDialog.Accepted:
        window = ESP32App()  # ← Ito ang Load Cell window na lalabas
        window.show()
        sys.exit(app.exec_())
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
