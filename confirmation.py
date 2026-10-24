from PySide6.QtWidgets import(QLabel,QWidget,QPushButton,QVBoxLayout,QGridLayout)
from PySide6.QtCore import Qt
from background import apply_blur_background,BUTTON_STYLE,LABEL_STYLE

SEAT_PRICE=250 #arbitary price. change later

class confirmation_window(QWidget):
    def __init__(self):
        super().__init__()#call the constructor 
        self.setWindowTitle("Booking Confirmation")

        #heading--------
        self.title=QLabel("Booking Confirmed!!!!")
        self.title.setStyleSheet("""
        font-family: "Georgia", "Times-New Roman", "serif";
        font-size: 44px; font-weight: 900; font-style: italic;
        color: #FFD700; padding: 16px;
        """)
        self.title.setAlignment(Qt.AlignCenter)

        # ---- checkmark / subtitle for extra breathing room under the title ----
        self.subtitle = QLabel("Here are your booking details!!!!")
        self.subtitle.setStyleSheet("font-size: 20px; color: #cccccc; padding-bottom: 10px;")
        self.subtitle.setAlignment(Qt.AlignCenter)


        #details--------
        self.details_label=QLabel("") #movie details,initially empty
        self.details_label.setStyleSheet(LABEL_STYLE)
        self.details_label.setAlignment(Qt.AlignCenter)

        #price details(initially empty)--------

        self.total_label=QLabel("")
        self.total_label.setStyleSheet("font-size: 26px; font-weight: 500; color: #FFD700;line-height: 180%;padding: 20px 30px;background: rgba(0, 0, 0, 110);border-radius: 10px;")
        self.total_label.setAlignment(Qt.AlignCenter)

        #BUTTONS

        self.done_button= QPushButton("Back to Home")
        self.done_button.setStyleSheet(BUTTON_STYLE)

        #layout------

        layout=QVBoxLayout()
        layout.setContentsMargins(60, 40, 60, 40)
        layout.setSpacing(18)
        layout.addStretch(1)
        layout.addWidget(self.title)
        layout.addWidget(self.subtitle)
        layout.addSpacing(10)
        layout.addWidget(self.details_label)
        layout.addSpacing(10)
        layout.addWidget(self.total_label)
        layout.addSpacing(20)
        layout.addWidget(self.done_button)
        layout.addStretch(2)

        apply_blur_background(self, layout, "assets/login_bg.jpg")

        #called after booking is confirmed-----

    def set_booking(self, movie,theatre,time,seats):
        seat_text = ", ".join(seats) if seats else "None"
        self.details_label.setText(
            f"Movie: {movie}\nTheatre: {theatre}\nShowtime: {time}\nSeats: {seat_text}"
        )
        total = len(seats) * SEAT_PRICE
        self.total_label.setText(f"Total Paid: ₹{total}")
     



