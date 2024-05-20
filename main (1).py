import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QListWidget, QMessageBox, QFileDialog
from ftplib import FTP
from PyQt5.QtCore import Qt


class FTPClient(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FTP Client")
        self.resize(600, 400)

        self.server_label = QLabel("FTP Server:")
        self.server_input = QLineEdit("ftp.dlptest.com")
        self.port_label = QLabel("Port:")
        self.port_input = QLabel("21")
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit("dlpuser")
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit("rNrKYTX9g7z3RgJRmxWuGHbeu")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.connect_button = QPushButton("Connect")
        self.connect_button.clicked.connect(self.connect_to_ftp)

        self.file_list = QListWidget()
        self.file_list.itemDoubleClicked.connect(self.download_file)

        self.upload_button = QPushButton("Upload")
        self.upload_button.clicked.connect(self.choose_file)

        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete_file)

        self.rename_label = QLabel("New Name:")
        self.rename_input = QLineEdit()
        self.rename_button = QPushButton("Rename")
        self.rename_button.clicked.connect(self.rename_file)

        layout = QVBoxLayout()
        server_layout = QHBoxLayout()
        server_layout.addWidget(self.server_label)
        server_layout.addWidget(self.server_input)
        server_layout.addWidget(self.port_label)
        server_layout.addWidget(self.port_input)
        layout.addLayout(server_layout)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.connect_button)
        layout.addWidget(self.file_list)
        layout.addWidget(self.upload_button)
        self.download_instruction_label = QLabel("<b>Double click to download the files!</b>")
        self.download_instruction_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.download_instruction_label)
        layout.addWidget(self.delete_button)
        rename_layout = QHBoxLayout()
        rename_layout.addWidget(self.rename_label)
        rename_layout.addWidget(self.rename_input)
        rename_layout.addWidget(self.rename_button)
        layout.addLayout(rename_layout)
        

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.ftp = None

    def connect_to_ftp(self):
        server = self.server_input.text()
        port = int(self.port_input.text())
        username = self.username_input.text()
        password = self.password_input.text()
        try:
            self.ftp = FTP()
            self.ftp.connect(server, port)
            self.ftp.login(username, password)
            self.update_file_list()
        except Exception as e:
            QMessageBox.warning(self, "Connection Error", str(e))

    def update_file_list(self):
        if self.ftp is not None:
            self.file_list.clear()
            files = self.ftp.nlst()
            for file in files:
                self.file_list.addItem(file)

    def download_file(self, item):
        filename = item.text()
        local_filename, _ = QFileDialog.getSaveFileName(self, "Save File", filename)
        if local_filename:
            with open(local_filename, 'wb') as f:
                self.ftp.retrbinary('RETR ' + filename, f.write)

    def choose_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Choose File")
        if filename:
            try:
                with open(filename, 'rb') as f:
                    self.ftp.storbinary('STOR ' + os.path.basename(filename), f)
                self.update_file_list()
            except Exception as e:
                QMessageBox.warning(self, "Upload Error", str(e))

    def delete_file(self):
        selected_items = self.file_list.selectedItems()
        if selected_items:
            filename = selected_items[0].text()
            try:
                self.ftp.delete(filename)
                QMessageBox.information(self, "File Deleted", f"File '{filename}' has been deleted.")
                self.update_file_list()
            except Exception as e:
                QMessageBox.warning(self, "Delete Error", str(e))
        else:
            QMessageBox.warning(self, "No File Selected", "Please select a file to delete.")

    def rename_file(self):
        selected_items = self.file_list.selectedItems()
        if selected_items:
            old_name = selected_items[0].text()
            new_name = self.rename_input.text()
            if new_name:
                try:
                    self.ftp.rename(old_name, new_name)
                    QMessageBox.information(self, "File Renamed", f"File '{old_name}' has been renamed to '{new_name}'.")
                    self.update_file_list()
                except Exception as e:
                    QMessageBox.warning(self, "Rename Error", str(e))
            else:
                QMessageBox.warning(self, "Invalid Name", "Please enter a valid new name.")
        else:
            QMessageBox.warning(self, "No File Selected", "Please select a file to rename.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    client = FTPClient()
    client.show()
    sys.exit(app.exec_())