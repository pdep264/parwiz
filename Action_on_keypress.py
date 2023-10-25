'''
A useful method to capture distinct keyboard press
and call another method to take appropriate action.
Here the result is just cmdline printed.
Also: Simple way to change text content of a label on button clicked.
But: To make it interesting, the text reverts after set number seconds.
Technique: could be used for flashing messages in message line.
        # Instead of just cmdline output, the eventFilter method can be used
        # to call other methods. Depending on key pressed viz: if event == 68
        # [which is d on keyboard] then delete foo or whatever enacted..
        # if obj is self and event.type() == QEvent.Type.KeyPress:
'''
from PyQt6.QtCore import QEvent, Qt, QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(400, 400, 500, 200)
        self.setWindowTitle("Event Handling")

        button = QPushButton("Click Me")
        button.clicked.connect(self.handle_button_click)
        vbox = QVBoxLayout()
        vbox.addWidget(button)

        self.label = QLabel("No button click yet")
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.installEventFilter(self)

        self.timeout_timer = QTimer(self)
        self.timeout_timer.timeout.connect(self.revert_text)

    def handle_button_click(self):
        self.label.setText("The button was clicked")
        self.timeout_timer.start(3000)  # 3000 ms (3 seconds)

    def revert_text(self):
        self.label.setText("Press the button")

    def eventFilter(self, obj, event):
        key_actions = {
            Qt.Key.Key_D: 'D key pressed',
            Qt.Key.Key_S: 'S key pressed',
            Qt.Key.Key_F: 'F key pressed'
        }
        if obj is self and event.type() == QEvent.Type.KeyPress:
            key = event.key()
            print(key_actions.get(key, "I don't know this key"))
            return True
        return super().eventFilter(obj, event)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
