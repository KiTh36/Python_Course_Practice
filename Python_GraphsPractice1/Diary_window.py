# This file contains the visual logic of the program
import os
import json
from datetime import datetime

from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

USER_DIR = "users"

MOODS = {
    "Happy": 5,
    "Neutral": 3,
    "Sad": 1
}

class DiaryWindow(QWidget):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.setWindowTitle(f"Mood Diary - {username}")
        self.setGeometry(400, 150, 700, 500)

        self.user_file = os.path.join(USER_DIR, f"{username}.json")
        self.load_data()

        self.init_ui()
        self.update_plot()

    def load_data(self):
        if os.path.exists(self.user_file):
            with open(self.user_file, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        else:
            self.data = {}

    def save_data(self):
        with open(self.user_file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def init_ui(self):
        main_layout = QHBoxLayout()

        mood_layout = QVBoxLayout()
        mood_layout.addWidget(QLabel("Select your mood:"))

        for mood, value in MOODS.items():
            btn = QPushButton(mood)
            btn.clicked.connect(lambda _, v=value: self.set_mood(v))
            mood_layout.addWidget(btn)

        main_layout.addLayout(mood_layout)

        self.figure, self.ax = plt.subplots(figsize=(5, 4))
        self.canvas = FigureCanvas(self.figure)
        main_layout.addWidget(self.canvas)

        self.setLayout(main_layout)

    def set_mood(self, value):
        today = datetime.now().strftime("%Y-%m-%d")
        self.data[today] = value
        self.save_data()
        self.update_plot()

    def update_plot(self):
        self.ax.clear()
        if self.data:
            dates = sorted(self.data.keys())
            moods = [self.data[d] for d in dates]
            self.ax.plot(dates, moods, marker="o")
            self.ax.set_ylim(0, 5)
            self.ax.set_title(f"{self.username}'s Mood Diary")
            self.figure.autofmt_xdate()
        self.canvas.draw()
