from PySide6.QtWidgets import( QApplication,QWidget, QLabel, QPushButton,QVBoxLayout,QHBoxLayout)
from background import apply_blur_background,HEADING_STYLE,BUTTON_STYLE,LABEL_STYLE

#converts a rating out of 10 into a 5-star string, e.g. 8 -> ★★★★☆
def make_stars(rating_out_of_10, max_stars=5):
    stars = round(rating_out_of_10 / 10 * max_stars)
    return "★" * stars + "☆" * (max_stars - stars)
 
 
# style for the star labels
STAR_STYLE = "font-size: 24px; color: #FFD700;"

# movie window class
class MoviesWindow(QWidget):
    #constructor
    def __init__(self):
        super().__init__() #constructor
        #window settings
        self.setWindowTitle("Movies")
        #movies titles

        self.movie_title=QLabel("What's Playing?")
        # bigger and bolder heading
        
        # bigger, bolder, stylish italic heading
        self.movie_title.setStyleSheet("""
        font-family: 'Georgia', 'Times New Roman', serif;
        font-size: 40px;
        font-weight: 900;
        font-style: italic;
        color: #FFD700;
        border-bottom: 3px solid #FFD700;
        padding: 8px;
        """)
        self.movie1=QLabel("Movie 1: Avengers")
        self.rating1=QLabel("Rating: 8")
        self.select_movie1=QPushButton("Select Movie")
        
        self.movie2=QLabel("Movie 2: Frozen ")
        self.rating2=QLabel("Rating: 8.5")
        self.select_movie2=QPushButton("Select Movie")
        
        self.movie3=QLabel("Movie 3: Parasite")
        self.rating3=QLabel("Rating: 8.2")
        self.select_movie3=QPushButton("Select Movie")
        
        self.movie4=QLabel("Movie 4: Interstellar")
        self.rating4=QLabel("Rating: 7")
        self.select_movie4=QPushButton("Select Movie")

        # apply label/button styling to all movie entries
        for label in (self.movie1,  self.movie2, 
            self.movie3,  self.movie4):
            label.setStyleSheet(LABEL_STYLE)

            # apply gold star styling to the ratings
        for label in (self.rating1, self.rating2, self.rating3, self.rating4):
            label.setStyleSheet(STAR_STYLE)

            #button styling

        for btn in (self.select_movie1, self.select_movie2, self.select_movie3, self.select_movie4):
            btn.setStyleSheet(BUTTON_STYLE)


        #all movies layout

        #movie1 layout
        movie1_layout=QVBoxLayout()
        movie1_layout.addWidget(self.movie1)
        movie1_layout.addWidget(self.rating1)
        movie1_layout.addWidget(self.select_movie1)
        
        #movie2 layout
        movie2_layout=QVBoxLayout()
        movie2_layout.addWidget(self.movie2)
        movie2_layout.addWidget(self.rating2)
        movie2_layout.addWidget(self.select_movie2)
        
        #movie3 layout
        movie3_layout=QVBoxLayout()
        movie3_layout.addWidget(self.movie3)
        movie3_layout.addWidget(self.rating3)
        movie3_layout.addWidget(self.select_movie3)
        
        #movie4 layout
        movie4_layout=QVBoxLayout()
        movie4_layout.addWidget(self.movie4)
        movie4_layout.addWidget(self.rating4)
        movie4_layout.addWidget(self.select_movie4)

        #movie horizontal layout
        movies_layout=QHBoxLayout()
        movies_layout.addLayout(movie1_layout)
        movies_layout.addLayout(movie2_layout)
        movies_layout.addLayout(movie3_layout)
        movies_layout.addLayout(movie4_layout) 
        
        #back button
        
        self.back_button=QPushButton("Back to Home")
        
        #main screen layout
        
        main_movie_layout=QVBoxLayout()
        main_movie_layout.addWidget(self.movie_title)
        main_movie_layout.addLayout(movies_layout)
        main_movie_layout.addWidget(self.back_button)
        
        #set blurred background

        apply_blur_background(self, main_movie_layout, "assets/login_bg.jpg")



