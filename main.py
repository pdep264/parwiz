from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
import sys
from PyQt6.uic import loadUiType

ui, _ = loadUiType('NotePadDemo.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)

        # Initialize the current file name as None
        self.current_file = None

        self.actionSave.triggered.connect(self.save_file)
        self.actionNew.triggered.connect(self.file_new)

    def modified_check(self):
        if not self.textEdit.document().isModified():
            return True

        ret = QMessageBox.warning(self, 'Application',
                                  'The document has been modified.\n'
                                  'Do you want to save your changes?',
                                  QMessageBox.StandardButton.Save |
                                  QMessageBox.StandardButton.Discard |
                                  QMessageBox.StandardButton.Cancel)

        if ret == QMessageBox.StandardButton.Save:
            return self.save_file()
        elif ret == QMessageBox.StandardButton.Discard:
            self.textEdit.clear()
        elif ret == QMessageBox.StandardButton.Cancel:
            return False

        return True

    def file_new(self):
        if self.modified_check():
            self.textEdit.clear()
            # Reset the current file name
            self.current_file = None

    def save_file(self):
        if self.current_file is None:
            # If no current file name exists, prompt for one
            filename, _ = QFileDialog.getSaveFileName(self, 'Save File')
            if not filename:
                return
            self.current_file = filename
        else:
            # If a current file name exists, use it
            filename = self.current_file

        with open(filename, 'w') as f:
            text = self.textEdit.toPlainText()
            f.write(text)
        # Update the status and show a message
        self.textEdit.document().setModified(False)
        QMessageBox.about(self, 'Save File', 'File has been saved')

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
