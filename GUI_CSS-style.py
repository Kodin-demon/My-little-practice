
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI")
        self.button_1 = QPushButton("#1")
        self.button_2 = QPushButton("#2")
        self.button_3 = QPushButton("#3")
        self.initUI()

    def initUI(self):

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hor_box = QHBoxLayout()

        hor_box.addWidget(self.button_1)
        hor_box.addWidget(self.button_2)
        hor_box.addWidget(self.button_3)

        central_widget.setLayout(hor_box)
        # we give each button a name
        self.button_1.setObjectName("button-001")
        self.button_2.setObjectName("button-002")
        self.button_3.setObjectName("button-003")

        self.setStyleSheet("""
            
            QPushButton{
                font-size: 48px;
                font-family: Comic Sans MS;
                padding: 20px 60px;
                margin: 30px;
                border: 3px solid;
                border-radius: 15px;
            }
            
            QPushButton#button-001{
                background-color: hsl(0, 98%, 56%);
            }
            QPushButton#button-002{
                background-color: hsl(61, 100%, 54%);
            }
            QPushButton#button-003{
                background-color: hsl(116, 87%, 50%);
            }
                     
            QPushButton#button-001:hover{
                background-color: hsl(0, 98%, 76%);
            }
            QPushButton#button-002:hover{
                background-color: hsl(61, 100%, 74%);
            }
            QPushButton#button-003:hover{
                background-color: hsl(116, 87%, 70%);
            }
        """) # first we decide how any button should look
             # then we choose a color separately for each button
             # at the end we choose a color when we hover over a button


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    #^^ it was just placed here, because there is no change needed