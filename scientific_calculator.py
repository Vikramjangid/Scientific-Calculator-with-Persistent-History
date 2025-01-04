import sys
import os
import math
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QGridLayout, QPushButton, QLineEdit, QListWidget, QHBoxLayout
)
from PyQt5.QtCore import Qt

HISTORY_FILE = "calc_history.txt"

class ScientificCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scientific Calculator")
        self.setFixedSize(500, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # Display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setStyleSheet("font-size: 24px; padding: 10px;")
        self.layout.addWidget(self.display)

        # Buttons and history layout
        main_layout = QHBoxLayout()
        self.layout.addLayout(main_layout)

        # Buttons
        self.buttons_widget = QWidget()
        self.buttons_layout = QGridLayout(self.buttons_widget)
        main_layout.addWidget(self.buttons_widget)

        self.create_buttons()
        self.bind_buttons()

        # History
        self.history_list = QListWidget()
        self.history_list.setStyleSheet("font-size: 18px; padding: 5px;")
        self.history_list.itemDoubleClicked.connect(self.load_from_history)
        main_layout.addWidget(self.history_list)

        self.current_expression = ""
        self.load_history()

    def create_buttons(self):
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'),
            ('sin', 'cos', 'tan', 'sqrt'),
            ('log', 'ln', '^', 'pi'),
            ('(', ')', 'C', 'AC'),
        ]

        for row, button_row in enumerate(buttons):
            for col, button_text in enumerate(button_row):
                button = QPushButton(button_text)
                button.setStyleSheet("font-size: 18px; padding: 15px;")
                self.buttons_layout.addWidget(button, row, col)

    def bind_buttons(self):
        for button in self.central_widget.findChildren(QPushButton):
            if button.text() == "=":
                button.clicked.connect(self.evaluate_expression)
            elif button.text() == "C":
                button.clicked.connect(self.clear_last)
            elif button.text() == "AC":
                button.clicked.connect(self.clear_all)
            else:
                button.clicked.connect(self.append_to_expression)

    def append_to_expression(self):
        button = self.sender()
        self.current_expression += button.text()
        self.display.setText(self.current_expression)

    def clear_last(self):
        self.current_expression = self.current_expression[:-1]
        self.display.setText(self.current_expression)

    def clear_all(self):
        self.current_expression = ""
        self.display.setText(self.current_expression)

    def evaluate_expression(self):
        try:
            expression = self.current_expression.replace('^', '**')
            expression = expression.replace('sqrt', 'math.sqrt')
            expression = expression.replace('log', 'math.log10')
            expression = expression.replace('ln', 'math.log')
            expression = expression.replace('pi', str(math.pi))
            expression = expression.replace('sin', 'math.sin')
            expression = expression.replace('cos', 'math.cos')
            expression = expression.replace('tan', 'math.tan')
            expression = expression.replace('e', str(math.e))

            result = eval(expression)
            result_str = f"{self.current_expression} = {result}"
            self.display.setText(str(result))
            self.current_expression = str(result)

            self.save_to_history(result_str)
        except Exception as e:
            self.display.setText("Error")
            self.current_expression = ""

    def save_to_history(self, expression):
        with open(HISTORY_FILE, "a") as file:
            file.write(expression + "\n")
        self.history_list.addItem(expression)

    def load_history(self):
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "r") as file:
                for line in file:
                    expression = line.strip()
                    self.history_list.addItem(expression)

    def load_from_history(self, item):
        self.current_expression = item.text().split(" = ")[0]
        self.display.setText(self.current_expression)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = ScientificCalculator()
    calculator.show()
    sys.exit(app.exec_())
