
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
# ^^ makes a bit easier with not writing all that every time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI, but with an image")
        self.setGeometry(700,350,600,500)

        label = QLabel(self)
        label.setGeometry(0,0,300,250)
        #^^ I assume that is self-explanatory

        pixmap = QPixmap("GUI_and_other_things/icon.png")
        label.setPixmap(pixmap)
        # ^^ first set pixmap and then add it to the label

        label.setScaledContents(True) # Important, without it will only display part of the image

        label.setGeometry((self.width() - label.width()) // 2,
                          (self.height() - label.height()) // 2,
                          # ^^ should allow placing inside the window. By dividing by 2 we get it in the middle
                          label.width(),label.height())
        #                   ^^ done to not manually write this again

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()