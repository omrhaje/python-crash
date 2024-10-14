# PyQt5 introduction
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        self.setGeometry(600, 300, 500, 500)
        self.setWindowIcon(QIcon("spiderman.png"))

        label = QLabel("Omar", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #f5b92f;"
                            "background-color: #063aa1;"
                            "font-weight: italic;"
                            "text-decoration: underline")

        # label.setAlignment(Qt.AlignTop) # VERTICALLY TOP
        # label.setAlignment(Qt.AlignBottom) # VERTICALLY BOTTOM
        # label.setAlignment(Qt.AlignVCenter) # VERTICALLY CENTER
        #
        # label.setAlignment(Qt.AlignRight) # HORIZONTALLY RIGHT
        # label.setAlignment(Qt.AlignLeft) # HORIZONTALLY LEFT
        # label.setAlignment(Qt.AlignHCenter) # HORIZONTALLY CENTER

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # CENTER | BOTTOM
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # CENTER | CENTER

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()