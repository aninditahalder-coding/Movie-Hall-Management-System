from PySide6.QtWidgets import(QLabel,QWidget, QScrollArea,QFrame,QHBoxLayout,QVBoxLayout,QPushButton)
from PySide6.QtCore import Qt
from background import apply_blur_background, BUTTON_STYLE

def make_avatar(initial, size=120):
    avatar=QLabel(initial.upper())
    avatar.setFixedSize(size,size)
    avatar.setAlignment(Qt.AlignCenter)
    avatar.setStyleSheet(f"""
        background: #f5c518;
        color: black;
        font-size: {size // 2}px;
        font-weight: 900;
        border-radius: {size // 2}px;
    """)
    return avatar


class profile_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Profile")
        
        # ---- card holding everything ----
        self.card = QFrame()
        self.card.setObjectName("card")
        self.card.setFixedWidth(600)
        self.card.setStyleSheet("""
            QFrame#card {
                background: rgba(0, 0, 0, 170);
                border: 2px solid #f5c518;
                border-radius: 16px;
            }
            """)
        
        #avatar + name

        self.avatar_label=make_avatar("👤")
        self.name_label=QLabel("")
        self.name_label.setAlignment(Qt.AlignCenter)
        self.name_label.setStyleSheet("""
            font-family: 'Georgia', 'Times New Roman', serif;
            font-size: 34px; font-weight: 900; font-style: italic;
            color: yellow; background: transparent;
        """)
        self.username_label=QLabel("")
        self.username_label.setAlignment(Qt.AlignCenter)
        self.username_label.setStyleSheet("font-size: 16px; color: #cccccc; background: transparent;")
        
        header_layout=QVBoxLayout()
        header_layout.setAlignment(Qt.AlignCenter)
        header_layout.setSpacing(10)
        header_layout.addWidget(self.avatar_label, alignment=Qt.AlignCenter)
        header_layout.addWidget(self.name_label)
        header_layout.addWidget(self.username_label)

        # ---- booking history heading ----
        self.history_heading = QLabel("🎟️ Booking History")
        self.history_heading.setStyleSheet("font-size: 22px; font-weight: 700; color: #FFD700; background: transparent;")

        # ---- scrollable list of booking cards ----
        self.list_layout = QVBoxLayout()
        self.list_layout.setSpacing(14)
        self.list_layout.addStretch(1)

        list_container = QWidget()
        list_container.setLayout(self.list_layout)
        list_container.setStyleSheet("background: transparent;")

        scroll = QScrollArea()
        scroll.setWidget(list_container)
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("background: transparent; border: none;")
        scroll.setFixedHeight(260)

        #buttons

        self.back_button = QPushButton("Back to Home")
        self.back_button.setStyleSheet(BUTTON_STYLE)
        self.back_button.setFixedWidth(220)

        # ---- card layout ----
 
        card_layout = QVBoxLayout(self.card)
        card_layout.setContentsMargins(40, 35, 40, 30)
        card_layout.setSpacing(16)
        card_layout.addLayout(header_layout)
        card_layout.addSpacing(10)
        card_layout.addWidget(self.history_heading)
        card_layout.addWidget(scroll)
        card_layout.addSpacing(6)
        card_layout.addWidget(self.back_button, alignment=Qt.AlignCenter)

        # ---- full-screen layout that centres the card ----

        page_layout = QVBoxLayout()
        page_layout.addStretch(1)
        page_layout.addWidget(self.card, alignment=Qt.AlignCenter)
        page_layout.addStretch(1)
 
        apply_blur_background(self, page_layout, "assets/login_bg.jpg")

    def make_booking_card(self,booking):
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background: rgba(255, 255, 255, 15);
                border: 1px solid #FFD700;
                border-radius: 10px;
            }
            """)
        movie_label = QLabel(f"🎬 {booking['movie']}")
        movie_label.setStyleSheet("font-size: 18px; font-weight: 700; color: yellow; background: transparent;")
 
        details_label = QLabel(
            f"{booking['theatre']}  •  {booking['time']}  •  Seats: {', '.join(booking['seats'])}"
        )
        details_label.setWordWrap(True)
        details_label.setStyleSheet(
            "font-size: 14px; color: white; background: transparent;")
 
        total_label = QLabel(f"₹{booking['total']}")
        total_label.setStyleSheet("font-size: 14px; font-weight: 700; color: #FFD700; background: transparent;")

        layout = QVBoxLayout(card)
        layout.setContentsMargins(16, 10, 16, 10)
        layout.setSpacing(4)
        layout.addWidget(movie_label)
        layout.addWidget(details_label)
        layout.addWidget(total_label)
        return card

    def _make_empty_state(self):
        empty = QLabel("No bookings yet — go catch a show! 🍿")
        empty.setAlignment(Qt.AlignCenter)
        empty.setStyleSheet("font-size: 16px; color: #cccccc; background: transparent; padding: 20px;")
        return empty

    # called by main.py every time the profile screen opens

    def set_profile(self, username, bookings):
        self.name_label.setText(username.capitalize())
        self.username_label.setText(f"@{username}")
        self.avatar_label.setText(username[:1].upper() if username else "?")
 
        # clear old cards (everything except the trailing stretch)
        while self.list_layout.count() > 1:
            item = self.list_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
 
        if not bookings:
            self.list_layout.insertWidget(0, self._make_empty_state())
            return
 
        for booking in reversed(bookings):
            self.list_layout.insertWidget(
                self.list_layout.count() - 1, self.make_booking_card(booking))
 



