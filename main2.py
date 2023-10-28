from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
import sys
from PyQt6.uic import loadUiType

ui, _ = loadUiType('NotePadDemo.ui')  # init instance for incoming Designer data

class MainApp(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)

        # signals
        self.actionSave.triggered.connect(self.save_file)
        self.actionNew.triggered.connect(self.file_new)

    def modified_check(self):
        if not self.textEdit.document().isModified():  # unmodified
            return True

        # otherwise the file is modified - check what to do with it
        ret = QMessageBox.warning(self, 'Application',
                                  'The document has been modified.\n'
                                  'Do you want to save your changes?',
                                  QMessageBox.StandardButton.Save |
                                  QMessageBox.StandardButton.Discard |
                                  QMessageBox.StandardButton.Cancel)

        if ret == QMessageBox.StandardButton.Save:
            return self.save_file()
        elif ret == QMessageBox.StandardButton.Discard:
            # clear text edit
            self.textEdit.clear()
        elif ret == QMessageBox.StandardButton.Cancel:
            return False

        return True

    def file_new(self):
        if self.modified_check():
            self.textEdit.clear()

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, 'Save File')
        if filename:
            with open(filename, 'w') as f:
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
