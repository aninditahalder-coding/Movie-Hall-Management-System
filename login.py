from PySide6.QtWidgets import( QApplication,QWidget, QLabel,QDialog,QLineEdit ,QGraphicsDropShadowEffect,QFrame,QMessageBox, QPushButton,QVBoxLayout,QHBoxLayout)
from PySide6.QtCore import Qt
from background import apply_blur_background, HEADING_STYLE,BUTTON_STYLE,LABEL_STYLE
import os
from PySide6.QtGui import QColor
from registration import REGISTERED_USERS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


#login window

class loginWindow(QDialog):
    def __init__(self):
        super().__init__()
        
        #window settings

        self.setWindowTitle("Login Box")

        # allow maximize button and maximized behavior on a QDialog
 
        self.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint)
        self.setWindowState(Qt.WindowMaximized)   # dialog opens full screen

        # ---- card (the small box in the middle) ----

        self.card = QFrame()
        self.card.setObjectName("card")
        self.card.setFixedWidth(480)
        self.card.setStyleSheet("""
            QFrame#card {
                background: rgba(0, 0, 0, 170);
                border: 2px solid #f5c518;
                border-radius: 16px;
            }
        """)
       

        #caption

        self.caption=QLabel("Lights , Camera, Action!!!!")
        self.caption.setAlignment(Qt.AlignCenter)
        self.caption.setStyleSheet("""
            font-size: 30px;
            font-weight: 800;
            color: #f5c518;
            padding: 10px;
        """)

        #subtittle

        self.subtitle=QLabel("Sign in to Continue Watching")
        self.subtitle.setAlignment(Qt.AlignCenter)
        self.subtitle.setStyleSheet("color: #888; font-size: 20px;")
        # soft dark shadow so the text stays readable on the photo
        for lbl in (self.caption, self.subtitle):
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(18)
            shadow.setOffset(3, 3)
            shadow.setColor(QColor(0, 0, 0, 230))
            lbl.setGraphicsEffect(shadow)

        # ---- inputs ----
        input_style = """
            QLineEdit {
                padding: 10px;
                border: 1px solid #cccccc;
                border-radius: 6px;
                font-size: 16px;
                background: white;
                color: black;
            }
            QLineEdit:focus {
                border: 2px solid #f5c518;
            }
        """

        #username field

        self.username_input=QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setStyleSheet(input_style)


        #password field
        self.password_input=QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet(input_style)

        
        #show/hide password toggle
        
        self.toggle_password_button=QPushButton("Show")
        self.toggle_password_button.setFixedWidth(64)
        self.toggle_password_button.setCheckable(True)
        self.toggle_password_button.setStyleSheet("""
            QPushButton {
                background-color: #444;
                color: white;
                border-radius: 6px;
                padding: 10px 6px;
                font-size: 14px;
            }
            QPushButton:checked { background-color: #666; }
        """)
        self.toggle_password_button.clicked.connect(self.toggle_password_visibility)
        password_row=QHBoxLayout()
        password_row.addWidget(self.password_input)
        password_row.addWidget(self.toggle_password_button)

         # ---- feedback label ----


        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("color: #ff6b6b; font-size: 14px; background: transparent;")
        
        #login button


        self.login_button=QPushButton("Login")
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: #f5c518;
                color: #000;
                font-weight: bold;
                border-radius: 6px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #ffd83d;
            }
            QPushButton:pressed {
                background-color: #d9ad0e;
            }
        """)

        #cancel button

        self.cancel_button=QPushButton("Cancel")
        self.cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #444;
                color: #fff;
                border-radius: 6px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #555;
            }
        """)


        #button row

        button_row=QHBoxLayout()
        button_row.addWidget(self.cancel_button)
        button_row.addWidget(self.login_button)

        # ---- sign-up link ----
        
        self.signup_link = QPushButton("New here? Sign Up")
        self.signup_link.setStyleSheet("""
            QPushButton {
                background: transparent;
                color: #f5c518;
                font-size: 14px;
                text-decoration: underline;
                border: none;
            }
            QPushButton:hover { color: #ffd83d; }
        """)
       
       # ---- layout inside the card ----
        card_layout = QVBoxLayout(self.card)
        card_layout.setContentsMargins(35, 30, 35, 30)
        card_layout.setSpacing(14)
        card_layout.addWidget(self.caption)
        card_layout.addWidget(self.subtitle)
        card_layout.addSpacing(10)
        card_layout.addWidget(self.username_input)
        card_layout.addLayout(password_row)
        card_layout.addWidget(self.status_label)
        card_layout.addLayout(button_row)
        card_layout.addWidget(self.signup_link, alignment=Qt.AlignCenter)

         # ---- full-screen layout that centres the card ----
        page_layout = QVBoxLayout()
        page_layout.addStretch(1)
        page_layout.addWidget(self.card, alignment=Qt.AlignCenter)
        page_layout.addStretch(1)

        #apply blurred image

        image_path = os.path.join(BASE_DIR, "assets", "login_bg.jpg")
        apply_blur_background(self, page_layout, image_path)

        

        #button connections

        self.login_button.clicked.connect(self.handle_login)
        self.cancel_button.clicked.connect(self.reject)
        self.password_input.returnPressed.connect(self.handle_login)
        self.username_input.returnPressed.connect(self.handle_login)

    #toggle password visibility

    def toggle_password_visibility(self):
        if self.toggle_password_button.isChecked():
            self.password_input.setEchoMode(QLineEdit.Normal)
            self.toggle_password_button.setText("Hide")
        else:
            self.password_input.setEchoMode(QLineEdit.Password)
            self.toggle_password_button.setText("Show")

    #handle login attempt

    def handle_login(self):
        username=self.username_input.text().strip()
        password=self.password_input.text().strip()
        print(f"DEBUG: username='{username}' password='{password}'")
        if not username or not password:
            self.status_label.setText("Please Enter both username and password")
            return


        # placeholder check — replace with real authentication logic


        if username in REGISTERED_USERS and REGISTERED_USERS[username] == password:
            self.status_label.setStyleSheet("color: #5cb85c; font-size: 11px;")
            self.status_label.setText("Login successful!")
            self.logged_in_username = username
            self.accept()
        else:
            self.status_label.setStyleSheet("color: #d9534f; font-size: 11px;")
            self.status_label.setText("Invalid username or password.")









 
 


