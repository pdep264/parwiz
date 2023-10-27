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
        self.actionNew.triggered.connect(self.file_new)



    def modified_check(self):
        if not self.textEdit.document().isModified:     # unmodified
            return True
        # otherwise the file is modified - check what to do with it
        ret = QMessageBox.warning(self, 'Application',
                                  'The ducument ahs been modified.\n'
                                  'Do you want to save your changes?',
                                  QMessageBox.StandardButton.Save |
                                  QMessageBox.StandardButton.Discard |
                                  QMessageBox.StandardButton.Cancel)
        if ret == QMessageBox.StandardButton.Save:
            return self.save_file()
        if ret == QMessageBox.StandardButton.Discard:
            self.textEdit.clear
        if ret == QMessageBox.StandardButton.Cancel:
            return False
        return True


    def file_new(self):
        if self.modified_check():
            self.textEdit.clear


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
