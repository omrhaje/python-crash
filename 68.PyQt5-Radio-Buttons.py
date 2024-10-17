import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup, QCheckBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        # Radio buttons for payment methods
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Mastercard", self)
        self.radio3 = QRadioButton("AMEX", self)
        self.radio4 = QRadioButton("Gift Card", self)
        self.radio5 = QRadioButton("Cash", self)

        # Initialize Button Groups
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)

        # In-store option, hidden by default
        self.in_store_checkbox = QCheckBox("In-store", self)
        self.in_store_checkbox.hide()  # Hidden initially

        # Call UI setup
        self.initUI()

    def initUI(self):
        # Set radio button positions
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)

        # Set in-store checkbox position
        self.in_store_checkbox.setGeometry(50, 250, 300, 50)

        # Set style for radio buttons
        self.setStyleSheet("QRadioButton {"
                           "font-size: 40px;"
                           "font-family: Italic;"
                           "padding: 10px;"
                           "}"
                           "QCheckBox {"
                           "font-size: 30px;"
                           "font-family: Arial;"
                           "padding: 10px;"
                           "}")

        # Add buttons to respective groups
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        # Connect radio buttons to the event handler
        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        # Check if "Gift Card" is selected
        if self.radio4.isChecked():
            print("Gift Card selected")
            self.in_store_checkbox.show()  # Show the "In-store" option
        else:
            self.in_store_checkbox.hide()  # Hide the "In-store" option

        # Print the selected payment method
        sender = self.sender()
        if sender.isChecked():
            print(f"{sender.text()} selected")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())