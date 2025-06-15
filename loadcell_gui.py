from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1318, 873)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # === Logo Image (top-left) ===
        self.logo_img = QtWidgets.QLabel(self.centralwidget)
        self.logo_img.setGeometry(QtCore.QRect(20, 20, 64, 64))
        logo_path = os.path.join("icons", "logo.png")
        self.logo_img.setPixmap(QtGui.QPixmap(logo_path))
        self.logo_img.setScaledContents(True)

        # === Logo Text (beside logo) ===
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(100, 30, 200, 40))
        self.logo_label.setText("WeighTrack")
        self.logo_label.setStyleSheet("font-weight: bold; font-size: 22pt;")
        self.logo_label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

        # === Top Menu Buttons ===
        button_y = 30
        button_width = 100
        spacing = 10
        start_x = 800

        self.btn_home = QtWidgets.QPushButton("Home", self.centralwidget)
        self.btn_home.setGeometry(QtCore.QRect(start_x, button_y, button_width, 30))

        self.btn_inventory = QtWidgets.QPushButton("Inventory", self.centralwidget)
        self.btn_inventory.setGeometry(QtCore.QRect(start_x + (button_width + spacing), button_y, button_width, 30))

        self.btn_sales = QtWidgets.QPushButton("Sales Report", self.centralwidget)
        self.btn_sales.setGeometry(QtCore.QRect(start_x + 2 * (button_width + spacing), button_y, button_width, 30))

        self.btn_notify = QtWidgets.QPushButton("Notification", self.centralwidget)
        self.btn_notify.setGeometry(QtCore.QRect(start_x + 3 * (button_width + spacing), button_y, button_width, 30))

        # === User Icon Button (top-right corner) ===
        self.btn_user = QtWidgets.QPushButton(self.centralwidget)
        self.btn_user.setGeometry(QtCore.QRect(start_x + 4 * (button_width + spacing) + 10, button_y, 30, 30))
        user_icon_path = os.path.join("icons", "profileicon.jpg")  # Use the correct icon path
        self.btn_user.setIcon(QtGui.QIcon(user_icon_path))
        self.btn_user.setIconSize(QtCore.QSize(30, 30))
        self.btn_user.setFlat(True)

        # === Center Table ===
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(150, 150, 1000, 600))
        self.table.setObjectName("table")
        self.table.setColumnCount(4)
        self.table.setRowCount(1)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table.verticalHeader().setVisible(False)

        # Set column headers
        self.table.setHorizontalHeaderLabels(["Product Name", "Shelf", "Weight", "Status"])

        # Dummy row setup
        for i in range(4):
            self.table.setItem(0, i, QtWidgets.QTableWidgetItem())

        # Final UI setup
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1318, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Load Cell Monitor"))
