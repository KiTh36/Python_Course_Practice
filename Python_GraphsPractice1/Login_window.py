# This file contains logic related to the login window
import os
import json
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from Diary_window import DiaryWindow

USER_DIR = "users"
os.makedirs(USER_DIR, exist_ok=True)

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Form")
        self.setGeometry(500, 200, 300, 150)
        self.setStyleSheet("background-color: #335C67;")

        self.label = QLabel("Enter your username:")
        self.label.setStyleSheet("color: #6564DB; font-size: 12pt;")

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(self.label)

        self.username_input = QLineEdit()
        layout.addWidget(self.username_input)

        btn_login = QPushButton("Continue")
        btn_login.clicked.connect(self.check_login)
        layout.addWidget(btn_login)

        btn_exit = QPushButton("Exit")
        btn_exit.clicked.connect(self.close)
        layout.addWidget(btn_exit)

        self.setLayout(layout)

    def check_login(self):
        username = self.username_input.text().strip()
        if not username:
            QMessageBox.warning(self, "Error", "Username cannot be empty")
            return

        user_file = os.path.join(USER_DIR, f"{username}.json")
        if not os.path.exists(user_file):
            answer = QMessageBox.question(
                self,
                "User not found",
                f"No diary for '{username}'. Create one?"
            )
            if not answer:
                return
            with open(user_file, "w", encoding="utf-8") as f:
                json.dump({}, f, ensure_ascii=False, indent=4)

        self.open_diary(username)

    def open_diary(self, username):
        self.close()
        self.diary = DiaryWindow(username)
        self.diary.show()
