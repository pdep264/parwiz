import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QLabel, QMainWindow, QTextEdit)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel('Click in this window')
        self.setCentralWidget(self.label)
        # self.label.setGeometry(100, 150, 200, 50)  # (x, y, width, height)

    def mouseMoveEvent(self, e):
        self.label.setText('mouseMoveEvent')

    def mousePressEvent(self, e):
        self.label.setText('mousePressEvent')

    def mouseReleaseEvent(self, e):
        self.label.setText('mouseReleaseEvent')

    def mouseDoubleClickEvent(self, e):
        self.label.setText('mouseDoubleClickEvent')


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
