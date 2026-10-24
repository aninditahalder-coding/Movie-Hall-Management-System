from PySide6.QtWidgets import( QApplication,QWidget, QLabel, QPushButton,QVBoxLayout,QHBoxLayout)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QGraphicsDropShadowEffect
from background import apply_blur_background,HEADING_STYLE,BUTTON_STYLE
#home window clASS

class HomeWindow(QWidget):
    #constructor
    def __init__(self):
        super().__init__()#call the constructor 
        #window settings
        
        self.setWindowTitle("Movies Ticket Booking System")


        
        # ---- profile button (top-right corner) ----


        self.profile_button = QPushButton("👤")
        self.profile_button.setFixedSize(48, 48)
        self.profile_button.setStyleSheet("""
            QPushButton {
                background: #f5c518;
                color: black;
                font-size: 20px;
                font-weight: 900;
                border-radius: 24px;
            }
            QPushButton:hover { background: #ffd83d; }
        """)
 
        top_bar = QHBoxLayout()
        top_bar.addStretch(1)          # pushes the button to the right
        top_bar.addWidget(self.profile_button)
 
        
        #Home screen layouts

        self.title=QLabel("It all starts here\nBook.Watch.Enjoy!!! ;)")

        # big, bold, stylish title
        self.title.setStyleSheet("""
        font-family: 'Georgia', 'Times New Roman', serif;
        font-size: 56px;
        font-weight: 900;
        font-style: italic;
        color: #FFD700;
        background: rgba(0, 0, 0, 120);
        border-bottom: 4px solid #FFD700;
        border-radius: 6px;
        padding: 20px;
        """)
        self.title.setAlignment(Qt.AlignCenter)
        # drop shadow for extra depth
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setOffset(4, 4)
        shadow.setColor(QColor(0, 0, 0, 220))
        self.title.setGraphicsEffect(shadow)

        #headings
        self.browse_button=QPushButton("Movie Zone")
        self.booking_button=QPushButton("MY Bookings")
        self.exit_button=QPushButton("Exit")

        #for styling

        for btn in (self.browse_button, self.booking_button, self.exit_button):
            btn.setStyleSheet(BUTTON_STYLE)

        #HOME SCREEN LAYOUT
        layout=QVBoxLayout()

        # top bar with the profile button
        layout.addLayout(top_bar)

        #Add title
        layout.addWidget(self.title)

        #browse movie button
        layout.addWidget(self.browse_button)

        #add my booking buttons
        layout.addWidget(self.booking_button)

        #add exit button
        layout.addWidget(self.exit_button)

        #add blur background
        apply_blur_background(self, layout, "assets/login_bg.jpg")

        #button connections
        self.exit_button.clicked.connect(self.close)








