# the program doesn't look that hard, but I would be long till I could figure that on my own

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        # I place these in init
        self.setWindowTitle("Digital Clock")
        self.setGeometry(725, 500, 550, 175)
        # variables that I will need a bit later
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        # a funktion for main part of the code
        self.initUI()

    def initUI(self):
        # defining place of our clock
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        # size and style of text and background
        self.time_label.setStyleSheet("font-size: 98px;"
                                      "font-family: Courier New;"
                                      "color: #69aa6b")
        self.setStyleSheet("background-color: #1e1f22;")
        # to update clock every second we use this
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        # funktion to show real time
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())