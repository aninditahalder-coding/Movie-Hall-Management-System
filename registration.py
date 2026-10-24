from PySide6.QtWidgets import (QLabel, QDialog, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QFrame, QGraphicsDropShadowEffect)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from background import apply_blur_background
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

REGISTERED_USERS = {"admin": "admin"}

class sign_up_window(QDialog):
    def __init__(self):
        super().__init__()

        # Window setup
        self.setWindowTitle("Sign up")
        self.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint)
        self.setWindowState(Qt.WindowMaximized)

        # Catchy headlines
        self.caption = QLabel("Join the Show!!")
        self.caption.setAlignment(Qt.AlignCenter)
        self.caption.setStyleSheet("""
            font-family: 'Georgia', 'Times New Roman', serif;
            font-size: 60px;
            font-weight: 900;
            font-style: italic;
            color: yellow;
            background: transparent;
        """)
        
        self.subtitle = QLabel("Create an account to start booking")
        self.subtitle.setAlignment(Qt.AlignCenter)
        self.subtitle.setStyleSheet("color: white; font-size: 22px; font-weight: 600; background: transparent;")

        # Drop shadows for labels (Corrected loop indentation)
        for lbl in (self.caption, self.subtitle):
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(18)
            shadow.setOffset(3, 3)
            shadow.setColor(QColor(0, 0, 0, 230))
            lbl.setGraphicsEffect(shadow)

        # Card (the small box in the middle)
        self.card = QFrame()
        self.card.setObjectName("Card")
        self.card.setFixedWidth(480)
        self.card.setStyleSheet("""
            QFrame#Card {
                background: rgba(0, 0, 0, 170);
                border: 2px solid #f5c518;
                border-radius: 16px;
            }
        """)

        input_style = """QLineEdit {
            padding: 10px;
            border: 1px solid #cccccc;
            border-radius: 6px;
            font-size: 16px;
            background: white;
            color: black;
        }
        QLineEdit:focus {
            border: 2px solid #f5c518;
        }"""

        # Inputs
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Choose a username")
        self.username_input.setStyleSheet(input_style)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Choose a password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet(input_style)

        self.confirm_input = QLineEdit(self)
        self.confirm_input.setPlaceholderText("Confirm password")
        self.confirm_input.setEchoMode(QLineEdit.Password)
        self.confirm_input.setStyleSheet(input_style)

        # Show/hide password button
        self.toggle_password = QPushButton("Show")
        self.toggle_password.setFixedWidth(60)
        self.toggle_password.setCheckable(True)
        self.toggle_password.setStyleSheet("""QPushButton {
            background-color: #444;
            color: white;
            border-radius: 6px;
            padding: 10px 6px;
            font-size: 14px;
            }
            QPushButton:checked { background-color: #666; }
        """)
        self.toggle_password.clicked.connect(self.toggle_password_visibility)
        
        password_row = QHBoxLayout()
        password_row.addWidget(self.password_input)
        password_row.addWidget(self.toggle_password)
        
        # Feedback label
        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("color: #ff6b6b; font-size: 14px; background: transparent;")
        
        # Buttons
        self.signup_button = QPushButton("Sign Up")
        self.signup_button.setStyleSheet("""
            QPushButton {
                background-color: #f5c518;
                color: #000;
                font-size: 18px;
                font-weight: bold;
                border-radius: 6px;
                padding: 10px;
            }
            QPushButton:hover { background-color: #ffd83d; }
            QPushButton:pressed { background-color: #d9ad0e; }
        """)
        
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setStyleSheet("""
            QPushButton {
            background-color: #444;
            color: #fff;
            font-size: 18px;
            border-radius: 6px;
            padding: 10px;
            }
            QPushButton:hover { background-color: #555; }
        """)
        
        button_row = QHBoxLayout()
        button_row.addWidget(self.signup_button)
        button_row.addWidget(self.cancel_button)
        
        # Layout inside the card
        card_layout = QVBoxLayout(self.card)
        card_layout.setContentsMargins(35, 30, 35, 30)
        card_layout.setSpacing(14)
        card_layout.addWidget(self.username_input)
        card_layout.addLayout(password_row)
        card_layout.addWidget(self.confirm_input)
        card_layout.addWidget(self.status_label)
        card_layout.addLayout(button_row)
        
        # Full-screen layout that centres the headline + card
        page_layout = QVBoxLayout()
        page_layout.addStretch(1)
        page_layout.addWidget(self.caption)
        page_layout.addWidget(self.subtitle)
        page_layout.addSpacing(30)
        page_layout.addWidget(self.card, alignment=Qt.AlignCenter)
        page_layout.addStretch(1)
        
        image_path = os.path.join(BASE_DIR, "assets", "login_bg.jpg")
        apply_blur_background(self, page_layout, image_path)
        
        # Button connections (Now safe because signup_button is instantiated properly)
        self.signup_button.clicked.connect(self.handle_signup)
        self.cancel_button.clicked.connect(self.reject)
        self.confirm_input.returnPressed.connect(self.handle_signup)
             
    def toggle_password_visibility(self):
        if self.toggle_password.isChecked():
            mode = QLineEdit.Normal
            self.toggle_password.setText("Hide")
        else:
            mode = QLineEdit.Password
            self.toggle_password.setText("Show")
        self.password_input.setEchoMode(mode)
        self.confirm_input.setEchoMode(mode)

    def handle_signup(self):
        username = self.username_input.text().strip()
        password = self.password_input.text()
        confirm = self.confirm_input.text()
 
        if not username or not password or not confirm:
            self.status_label.setText("Please fill in every field")
            return
 
        if len(username) < 3:
            self.status_label.setText("Username must be at least 3 characters")
            return
 
        if username in REGISTERED_USERS:
            self.status_label.setText("That username is already taken")
            return
 
        if len(password) < 4:
            self.status_label.setText("Password must be at least 4 characters")
            return
 
        if password != confirm:
            self.status_label.setText("Passwords do not match")
            return
 
        REGISTERED_USERS[username] = "admin"
        self.accept()