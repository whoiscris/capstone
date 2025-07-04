import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import QTimer
from loadcell_gui import Ui_MainWindow  # your generated GUI class
import Inventory_gui  # ← Make sure this exists in the same folder


class ESP32App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ip_address = "http://192.168.133.148/"  # Replace with your ESP32 IP if it changes

        # Set up a timer to auto-refresh every 2 seconds
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_table)
        self.timer.start(2000)  # 2000 milliseconds = 2 seconds

        self.update_table()  # Initial fetch

        # === Connect Inventory button ===
        self.ui.btn_inventory.clicked.connect(self.open_inventory)

    def update_table(self):
        try:
            response = requests.get(self.ip_address, timeout=5)
            data = response.json()

            self.ui.table.setRowCount(1)
            self.ui.table.setItem(0, 0, QTableWidgetItem(data["product"]))
            self.ui.table.setItem(0, 1, QTableWidgetItem(data["shelf"]))
            self.ui.table.setItem(0, 2, QTableWidgetItem(str(data["weight"])))
            self.ui.table.setItem(0, 3, QTableWidgetItem(data["status"]))
        except Exception as e:
            QMessageBox.critical(self, "Connection Error", f"Could not connect to ESP32:\n{e}")

    def open_inventory(self):
        self.inventory_window = Inventory_gui.InventoryWindow()
        self.inventory_window.center_window()
        self.inventory_window.show()
        self.close()

    def center_window(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ESP32App()
    window.center_window()  # Optional: center the app on launch
    window.show()
    sys.exit(app.exec_())
