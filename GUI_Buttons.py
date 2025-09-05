
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI")
        self.setGeometry(700,350,600,500)
        self.button = QPushButton("Click", self)
        self.label = QLabel("Good evening", self)
        self.initUI()

    def initUI(self):
        # Button
        self.button.setGeometry(225, 200,150, 100)
        self.button.clicked.connect(self.on_click)
        # Label //Text//
        self.label.setGeometry(150,0,300,250)
        self.label.setStyleSheet("font-size: 30px;")

    def on_click(self):
        # Button after click
        print("Button was clicked")
        self.button.setText("Clicked!!!")
        # Label after click
        self.button.setDisabled(True)
        self.label.setText("Have a good day")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()