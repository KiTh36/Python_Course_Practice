# This file starts the program
import sys
from PyQt6.QtWidgets import QApplication
from Login_window import LoginWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
