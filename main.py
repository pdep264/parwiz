# from PyQt6.QtCore import *
# from PyQt6.QtGui import *
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
import sys
from PyQt6.uic import loadUiType

ui, _ = loadUiType('NotePadDemo.ui')  # init instance for incoming Designer data


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show

        # signals
        self.actionSave.triggered.connect(self.save_file)

    def save_file(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File')
        if filename[0]:
            f = open(filename[0], 'w')
        with f:
            text = self.textEdit.toPlainText()
            f.write(text)
            QMessageBox.about(self, 'Save File', 'File has been saved')


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
