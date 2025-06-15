from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
import sys
import loadcell_gui  # Import the Home GUI setup
import mains_gui  # Import the ESP32App for Home navigation


class InventoryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventory")
        self.setGeometry(100, 100, 1318, 873)
        self.center_window()  # ← Auto-center on screen

        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        # === Logo Icon ===
        self.logo_img = QLabel(self.centralwidget)
        self.logo_img.setGeometry(QtCore.QRect(20, 20, 64, 64))
        self.logo_img.setPixmap(QtGui.QPixmap("icons/logo.png"))
        self.logo_img.setScaledContents(True)

        # === WeighTrack Title ===
        self.logo_label = QLabel("WeighTrack", self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(100, 30, 200, 40))
        self.logo_label.setStyleSheet("font-weight: bold; font-size: 22pt;")
        self.logo_label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

        # === Navigation Buttons ===
        button_y = 30
        button_width = 100
        spacing = 10
        start_x = 800

        self.btn_home = QPushButton("Home", self.centralwidget)
        self.btn_home.setGeometry(QtCore.QRect(start_x, button_y, button_width, 30))
        self.btn_home.clicked.connect(self.go_home)

        self.btn_inventory = QPushButton("Inventory", self.centralwidget)
        self.btn_inventory.setGeometry(QtCore.QRect(start_x + (button_width + spacing), button_y, button_width, 30))
        # current window, no action needed

        self.btn_sales = QPushButton("Sales Report", self.centralwidget)
        self.btn_sales.setGeometry(QtCore.QRect(start_x + 2 * (button_width + spacing), button_y, button_width, 30))

        self.btn_notify = QPushButton("Notification", self.centralwidget)
        self.btn_notify.setGeometry(QtCore.QRect(start_x + 3 * (button_width + spacing), button_y, button_width, 30))

        # === User Profile Icon ===
        self.btn_user = QPushButton(self.centralwidget)
        self.btn_user.setGeometry(QtCore.QRect(start_x + 4 * (button_width + spacing) + 10, button_y, 30, 30))
        self.btn_user.setIcon(QtGui.QIcon("icons/profileicon.jpg"))
        self.btn_user.setIconSize(QtCore.QSize(30, 30))
        self.btn_user.setFlat(True)

        # === Inventory Page Content (Centered Label) ===
        self.label = QLabel("Inventory Page", self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 300, 50))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 18pt; font-weight: bold;")
        self.label.move(
            (self.width() - self.label.width()) // 2,
            (self.height() - self.label.height()) // 2
        )

    def go_home(self):
        self.hide()
        self.home_window = mains_gui.ESP32App()
        self.home_window.center_window()  # center home window too
        self.home_window.show()

    def center_window(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryWindow()
    window.show()
    sys.exit(app.exec_())
