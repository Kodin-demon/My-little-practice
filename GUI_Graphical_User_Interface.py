
import sys

import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.setWindowIcon(PyQt5.QtGui.QIcon("icon.png"))
        #                  ^^ why do I have to do all this to  just get an icon for GUI
        self.setGeometry(700,350,600,500) # It is roughly in the middle of my screen //1980x1080//

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    #^^ Things that allow you to create, show and hold it in place

if __name__ == "__main__":
    main()