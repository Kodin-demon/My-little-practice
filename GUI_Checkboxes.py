
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI")
        self.setGeometry(700,350,600,500)
        self.checkbox = QCheckBox("Leave a 'Title Card' here", self)
        self.initUI()

    def initUI(self):

        self.checkbox.setGeometry(10, 0, 350, 100) # without it the text will be cropped
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Arial;")

        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checker_box)
        # ^^ important to connect slots //I assume everything in GUI ocupy a slot//

    def checker_box(self, state):
        # ^^ as always we create a function for every thing we do to not get messy
        if state == Qt.Checked:
            #       ^^ when checked it leaves a value of 2, but for readability we use this
            print("You left a 'Title Card'")
        else:
            print("You left nothing")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()