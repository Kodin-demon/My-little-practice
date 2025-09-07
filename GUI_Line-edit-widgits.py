
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Write something if you may")
        self.setGeometry(700,350,600,500)
        # just a bit of separation to look better
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)

        self.initUI()

    def initUI(self):
        # adjusting place and size
        self.line_edit.setGeometry(5,5,300,50)
        self.button.setGeometry(310,5,100,50)
        # setting a style
        self.line_edit.setStyleSheet("font-size: 24px;"
                                     "font-family: Comic Sans MS;") # Wingdings for fun if you may
        self.button.setStyleSheet("font-size: 24px;"
                                  "font-family: Comic Sans MS;")
        # placing a placeholder text
        self.line_edit.setPlaceholderText("IDK, write something")
        # connecting button to a function
        self.button.clicked.connect(self.submit)

    def submit(self):
        text = self.line_edit.text()
        print(f"Your Submission: {text}")
        # ^^ doing something with an input


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()