from PySide6.QtWidgets import (QWidget, QLabel, QPushButton,QVBoxLayout,QHBoxLayout,QFrame,QScrollArea)
from PySide6.QtCore import Qt
from background import apply_blur_background, BUTTON_STYLE

class my_bookings_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Bookings")

        self.title=QLabel("Your Movie Journey 🎬")
        self.title.setStyleSheet("""
            font-family: 'Georgia', 'Times New Roman', serif;
            font-size: 52px; font-weight: 900; font-style: italic;
            color: yellow; background: transparent;""")
        self.title.setAlignment(Qt.AlignCenter)

        self.subtitle=QLabel("Every Great Story Deserves an Encore")
        self.subtitle.setStyleSheet("font-size: 20px; color: #dddddd; background: transparent;")
        self.subtitle.setAlignment(Qt.AlignCenter)

        #scrollable list or area

        self.list_layout= QVBoxLayout()
        self.list_layout.setSpacing(18)
        self.list_layout.addStretch(1)   # keeps cards pinned to the top as more are added

        list_container=QWidget()
        list_container.setLayout(self.list_layout)
        list_container.setStyleSheet("background: transparent;")

        scroll=QScrollArea()
        scroll.setWidget(list_container)
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("background: transparent; border: none;")
        scroll.setFixedWidth(800)

        #back button

        self.back_button = QPushButton("Back to Home")
        self.back_button.setStyleSheet(BUTTON_STYLE)
        self.back_button.setFixedWidth(220)

        # ---- page layout ----

        page_layout = QVBoxLayout()
        page_layout.setContentsMargins(40, 40, 40, 40)
        page_layout.addWidget(self.title)
        page_layout.addWidget(self.subtitle)
        page_layout.addSpacing(20)
        page_layout.addWidget(scroll, alignment=Qt.AlignCenter)
        page_layout.addSpacing(10)
        page_layout.addWidget(self.back_button, alignment=Qt.AlignCenter)
 
        apply_blur_background(self, page_layout, "assets/login_bg.jpg")

    def make_card(self,booking):
        card=QFrame()
        card.setStyleSheet("""
            QFrame {
                background: rgba(0, 0, 0, 150);
                border: 2px solid #FFD700;
                border-radius: 14px;
            }
        """)   
        movie_label = QLabel(f"🎬 {booking['movie']}") #formats the movie titles
        movie_label.setStyleSheet("""
            font-size: 26px; font-weight: 800; color: yellow;
            background: transparent;
        """)

        details_label = QLabel(
            f"🏛️ {booking['theatre']}   •   🕒 {booking['time']}   •   "
            f"💺 {', '.join(booking['seats'])}"
        )
        details_label.setWordWrap(True)
        details_label.setStyleSheet("font-size: 18px; color: white; background: transparent;")
 
        total_label = QLabel(f"💰 Total Paid: ₹{booking['total']}")
        total_label.setStyleSheet("font-size: 18px; font-weight: 700; color: #FFD700; background: transparent;")

        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(24, 18, 24, 18)
        card_layout.setSpacing(8)
        card_layout.addWidget(movie_label)
        card_layout.addWidget(details_label)
        card_layout.addWidget(total_label)

        return card

    def _make_empty_state(self):
        empty = QLabel("No bookings yet! Time to catch a show 🍿")
        empty.setAlignment(Qt.AlignCenter)
        empty.setStyleSheet("""
            font-size: 24px; font-weight: 600; color: #dddddd;
            background: transparent; padding: 40px;
        """)
        return empty

    # called by main.py every time the My Bookings screen opens
    def set_bookings(self, bookings):
        # clear out the old cards (everything except the trailing stretch)
        while self.list_layout.count() > 1:
            item = self.list_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
 
        if not bookings:
            self.list_layout.insertWidget(0, self._make_empty_state())
            return
 
        # newest booking first
        for booking in reversed(bookings):
            self.list_layout.insertWidget(self.list_layout.count() - 1, self.make_card(booking))


 

      

