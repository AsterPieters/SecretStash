import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit

from authenticate import authenticate_user


class LoginPage(QWidget):
    def __init__(self):
        super().__init__()

        self.init()

    def init(self):

        ##### window properties #####
        self.setGeometry(2500, 100, 1000, 800)
        self.setWindowTitle('SecretStash')

        ##### Login textfield #####
        self.password_field = QLineEdit(self)
        self.password_field.setEchoMode(QLineEdit.Password)
        self.password_field.setPlaceholderText('Enter your password...')
        
        ##### Login button #####
        self.login_button = QPushButton('Click me', self)
        self.login_button.clicked.connect(self.login_button_click)

        ##### Layout #####
        layout = QVBoxLayout()
        layout.addWidget(self.password_field)
        layout.addWidget(self.login_button)
        self.setLayout(layout)

        ##### Show #####
        self.show()

    def login_button_click(self):
        password = self.password_field.text()
        if authenticate_user(password):
            self.mainpage(password)
            QApplication.quit()