import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QVBoxLayout, QHBoxLayout, QGridLayout,
    QFormLayout, QStackedLayout, QLineEdit
)
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Layout Demo")
        self.resize(900, 600)

        main_layout = QVBoxLayout(self)

        # ---------- HEADER ----------
        header_layout = QHBoxLayout()
        for text, color in [("Header 1", "#ff7675"), ("Header 2", "#74b9ff")]:
            lbl = QLabel(text)
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            lbl.setStyleSheet(f"background:{color}; padding:20px; font-weight:bold;")
            header_layout.addWidget(lbl)
        main_layout.addLayout(header_layout)

        # ---------- CONTENT ----------
        content_layout = QVBoxLayout()

        # Navigation buttons
        nav_layout = QHBoxLayout()
        self.btn_grid = QPushButton("Grid page")
        self.btn_form = QPushButton("Form page")
        nav_layout.addWidget(self.btn_grid)
        nav_layout.addWidget(self.btn_form)
        content_layout.addLayout(nav_layout)

        # Stacked layout
        self.stacked = QStackedLayout()
        self.stacked.addWidget(self.create_grid_page())
        self.stacked.addWidget(self.create_form_page())
        content_layout.addLayout(self.stacked)

        main_layout.addLayout(content_layout)

        # Button connections
        self.btn_grid.clicked.connect(lambda: self.stacked.setCurrentIndex(0))
        self.btn_form.clicked.connect(lambda: self.stacked.setCurrentIndex(1))

    # ---------- PAGES ----------
    def create_grid_page(self):
        page = QWidget()
        grid = QGridLayout(page)
        for row in range(3):
            for col in range(3):
                lbl = QLabel(f"({row},{col})")
                lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl.setStyleSheet("border:1px solid gray; padding:10px;")
                grid.addWidget(lbl, row, col)
        return page

    def create_form_page(self):
        page = QWidget()
        form = QFormLayout(page)
        form.addRow("Name:", QLineEdit())
        form.addRow("Email:", QLineEdit())
        form.addRow("Password:", QLineEdit())
        form.addRow(QPushButton("Submit"))
        return page

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
