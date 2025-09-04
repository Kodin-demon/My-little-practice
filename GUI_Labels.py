
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI")
        self.setGeometry(700,350,600,500)
        label = QLabel("Hi there", self)
        label.setFont(QFont("Arial", 48))
        label.setGeometry(0,0,600,100)
        label.setStyleSheet("color: #013280;"
                            "background-color: #d8e1f0;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        # label.setAlignment(Qt.AlignTop)
        # label.setAlignment(Qt.AlignBottom)
        # label.setAlignment(Qt.AlignVCenter)
        # ^^ to control text vertically

        # label.setAlignment(Qt.AlignRight)
        # label.setAlignment(Qt.AlignHCenter)
        # label.setAlignment(Qt.AlignLeft)
        # ^^ to control text horizontally

        label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # Can also use both

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()