from PySide6.QtWidgets import (QLabel,QWidget,QFrame,QPushButton,QHBoxLayout,QVBoxLayout)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPainter, QColor, QFont, QPen 
from background import apply_blur_background , BUTTON_STYLE 
from movies import make_stars
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POSTER_DIR = os.path.join(BASE_DIR, "assets", "posters")

POSTER_W=300
POSTER_H=450

#sample data

MOVIE_DATA={
    "Avengers":{
        "rating":8,
        "views" :"2.5M Views",
        "cast": "Robert Downey Jr., Chris Evans, Scarlett Johansson, Mark Ruffalo",
        "description":"Earth's mightiest heroes must put their differences aside and team up to stop a powerful threat from wiping out humanity.",
    },
    "Frozen":{
        "rating":8.5,
        "views":"3.2M Views",
        "cast":"Elsa, Anna, Kristoff, Sven, and Olaf",
        "description":"Frozen follows Princess Anna on a quest through icy landscapes to save her kingdom and reconnect with her sister Elsa, whose magical powers have unleashed eternal winter.",

    },
    "Parasite":{
        "rating": 8.2,
        "views": "1.8M views",
        "cast": "Song Kang-ho, Lee Sun-kyun, Cho Yeo-jeong, Choi Woo-shik",
        "description": "A poor family schemes its way into the lives of a wealthy household, and things soon spiral out of control.",
    },
    "Interstellar":{
        "rating": 7,
        "views": "3.0M views",
        "cast": "Matthew McConaughey, Anne Hathaway, Jessica Chastain, Michael Caine",
        "description": "With Earth running out of time, a team of astronauts travels through a wormhole in search of a new home for humanity.",
    },
}

def make_placeholder_poster(title):
    pixmap=QPixmap(POSTER_H,POSTER_W)
    pixmap.fill(QColor("#1b1b2f"))
    painter=QPainter(pixmap)
    painter.setPen(QPen(QColor("#FFD700"), 6))
    painter.drawRect(3, 3, POSTER_W - 6, POSTER_H - 6)
    font = QFont("Georgia", 26)
    font.setBold(True)
    font.setItalic(True)
    painter.setFont(font)
    painter.setPen(QColor("#FFD700"))
    painter.drawText(pixmap.rect().adjusted(20, 20, -20, -20),Qt.AlignCenter | Qt.TextWordWrap, title)
    painter.end()
    return pixmap

class movie_details_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Movie Details")
        
        #card holding every details
        
        self.card=QFrame()
        self.card.setObjectName("Card")
        self.card.setStyleSheet("""
            QFrame#card {
            background: rgba(0, 0, 0, 170);
            border: 2px solid #FFD700;
            border-radius: 16px;}
            """)
        # Poster left
        
        self.poster_label=QLabel()
        self.poster_label.setFixedSize(POSTER_W,POSTER_H)
        self.poster_label.setAlignment(Qt.AlignCenter)
        self.poster_label.setStyleSheet("background: transparent; border-radius: 8px;")


        #text(right)

        self.name_label=QLabel("")
        self.name_label.setWordWrap(True)
        self.name_label.setStyleSheet("""
            font-family: 'Georgia', 'Times New Roman', serif;
            font-size: 46px; font-weight: 900; font-style: italic;
            color: yellow; background: transparent;
            """)

        self.rating_label = QLabel("")
        self.rating_label.setStyleSheet("font-size: 26px; color: #FFD700; background: transparent;")
             
        self.views_label = QLabel("")
        self.views_label.setStyleSheet("font-size: 20px; color: #dddddd; background: transparent;")

        self.cast_label = QLabel("")
        self.cast_label.setWordWrap(True)
        self.cast_label.setStyleSheet("font-size: 20px; color: white; background: transparent;")
            
        self.desc_heading = QLabel("About the movie")
        self.desc_heading.setStyleSheet("font-size: 22px; font-weight: 700; color: #FFD700; background: transparent;")

        self.desc_label=QLabel("")
        self.desc_label.setWordWrap(True)
        self.desc_label.setStyleSheet("font-size: 20px; color: white; background: transparent;")

        #buttons

        self.back_button = QPushButton("Back to Movies")
        self.book_button = QPushButton("Book Tickets")
        for b in (self.back_button, self.book_button):
            b.setStyleSheet(BUTTON_STYLE)
            
        button_row = QHBoxLayout()
        button_row.addWidget(self.back_button)
        button_row.addWidget(self.book_button)

        info_layout = QVBoxLayout()
        info_layout.setSpacing(12)
        info_layout.addWidget(self.name_label)
        info_layout.addWidget(self.rating_label)
        info_layout.addWidget(self.views_label)
        info_layout.addSpacing(6)
        info_layout.addWidget(self.cast_label)
        info_layout.addSpacing(6)
        info_layout.addWidget(self.desc_heading)
        info_layout.addWidget(self.desc_label)
        info_layout.addStretch(1)
        info_layout.addLayout(button_row)

        # ---- card layout: poster | info ---
        card_layout = QHBoxLayout(self.card)
        card_layout.setContentsMargins(40, 40, 40, 40)
        card_layout.setSpacing(40)
        card_layout.addWidget(self.poster_label, alignment=Qt.AlignTop)
        card_layout.addLayout(info_layout)
        self.card.setFixedWidth(1000)

        # ---- full-screen layout that centres the card ----
        page_layout = QVBoxLayout()
        page_layout.addStretch(1)
        page_layout.addWidget(self.card, alignment=Qt.AlignCenter)
        page_layout.addStretch(1)
        apply_blur_background(self, page_layout, "assets/login_bg.jpg")

        # called by main.py every time a movie is picked
    def set_movie(self, name):
        data = MOVIE_DATA.get(name, {"rating": 0, "views": "", "cast": "Cast details coming soon","description": "Description coming soon.",})
                
        self.name_label.setText(name)
        self.rating_label.setText(f"{make_stars(data['rating'])}   {data['rating']}/10")
        self.views_label.setText(f"👁 {data['views']}" if data["views"] else "")
        self.cast_label.setText(f"<b>Cast:</b> {data['cast']}")
        self.desc_label.setText(data["description"])
                
                
        # poster: use the image file if it exists, otherwise a drawn placeholder
                
        file_name = name.lower().replace(" ", "_") + ".jpg"
        poster_path = os.path.join(POSTER_DIR, file_name)
        pixmap = QPixmap(poster_path) if os.path.exists(poster_path) else QPixmap()
        if pixmap.isNull():
            pixmap = make_placeholder_poster(name)
        self.poster_label.setPixmap(pixmap.scaled(POSTER_W, POSTER_H, Qt.KeepAspectRatio, Qt.SmoothTransformation))
 
            
            
 





            


