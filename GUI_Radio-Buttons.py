
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI")
        self.setGeometry(700,350,600,500)
        self.radio_1 = QRadioButton("Sleep", self)
        self.radio_2 = QRadioButton("Lunch", self)
        self.radio_3 = QRadioButton("Games", self)
        self.radio_4 = QRadioButton("Yourself", self)
        self.radio_5 = QRadioButton("Your Friend", self)
        #^^ declaring every button
        self.button_group_1 = QButtonGroup(self)
        self.button_group_2 = QButtonGroup(self)
        #^^ also creating different groups 
        self.initUI()

    def initUI(self):
        # Geometry for every radio button
        self.radio_1.setGeometry(0, 0, 400, 75)
        self.radio_2.setGeometry(0, 75, 400, 75)
        self.radio_3.setGeometry(0, 150, 400, 75)
        self.radio_4.setGeometry(0, 225, 400, 75)
        self.radio_5.setGeometry(0, 300, 400, 75)
        # Setting a style for all of them
        self.setStyleSheet("QRadioButton{"
                           "font-size: 40px;"
                           "padding: 15px;"
                           "}")
        # Group 1
        self.button_group_1.addButton(self.radio_1)
        self.button_group_1.addButton(self.radio_2)
        self.button_group_1.addButton(self.radio_3)
        # Group 2
        self.button_group_2.addButton(self.radio_4)
        self.button_group_2.addButton(self.radio_5)
        # Connecting it to a function
        self.radio_1.toggled.connect(self.change_radio_button)
        self.radio_2.toggled.connect(self.change_radio_button)
        self.radio_3.toggled.connect(self.change_radio_button)
        self.radio_4.toggled.connect(self.change_radio_button)
        self.radio_5.toggled.connect(self.change_radio_button)

    def change_radio_button(self):

        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"You choose: {radio_button.text()}")
        #^^ This all should tell us which button was chosen

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":

    main()
