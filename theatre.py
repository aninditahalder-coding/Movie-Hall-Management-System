from PySide6.QtWidgets import( QApplication,QWidget, QLabel, QPushButton,QVBoxLayout,QHBoxLayout)
from PySide6.QtCore import Qt
from background import apply_blur_background,HEADING_STYLE,BUTTON_STYLE,LABEL_STYLE
#theatre window class

class theatrewindow(QWidget):
    def __init__(self):
        super().__init__()

        #window settings
        
        self.setWindowTitle("Theatre and show selection")
       
        
        # theatre screen title (custom size, bigger/bolder than the shared HEADING_STYLE)

        self.theatre_title = QLabel("Select Theatre and show")
        self.theatre_title.setStyleSheet("""
        font-family: 'Georgia', 'Times New Roman', serif;
        font-size: 40px;
        font-weight: 900;
        font-style: italic;
        color: #FFD700;
        border-bottom: 3px solid #FFD700;
        padding: 8px;
        """)
        self.theatre_title.setAlignment(Qt.AlignCenter)

        #theatre options
        self.theatre1=QPushButton("Screen1")
        self.theatre2=QPushButton("Screen 2")
        self.theatre3=QPushButton("Screen 3")
        self.theatre4=QPushButton("Screen 4")
        self.theatre5=QPushButton("Screen 5")


        #theatre timings
        self.show1=QPushButton("10:00 AM")
        self.show2=QPushButton("2:00 PM")
        self.show3=QPushButton("5:00 AM")
        self.show4=QPushButton("8:00 AM")
        self.show5=QPushButton("11:00 AM")

        for btn in (self.theatre1, self.theatre2,self.theatre3,self.theatre4,self.theatre5 ,self.show1, self.show2,self.show3, self.show4, self.show5):btn.setStyleSheet(BUTTON_STYLE)

        self.show_time_label = QLabel("Select Show Time")
        self.show_time_label.setStyleSheet(LABEL_STYLE)

        #theatre options layout (horizontal)

        theatre_options_layout=QHBoxLayout()
        theatre_options_layout.addWidget(self.theatre1)
        theatre_options_layout.addWidget(self.theatre2)
        theatre_options_layout.addWidget(self.theatre3)
        theatre_options_layout.addWidget(self.theatre4)
        theatre_options_layout.addWidget(self.theatre5)
        



        #theatre layout

        theatre_layout=QVBoxLayout()
        theatre_layout.addWidget(self.theatre_title)
        theatre_layout.addLayout(theatre_options_layout)
        theatre_layout.addWidget(self.show_time_label)
        theatre_layout.addWidget(self.show1)
        theatre_layout.addWidget(self.show2)
        theatre_layout.addWidget(self.show3)
        theatre_layout.addWidget(self.show4)
        theatre_layout.addWidget(self.show5)

        #back button

        self.theatre_back=QPushButton("Back to Movies")
        theatre_layout.addWidget(self.theatre_back)

        #apply blurred image

        apply_blur_background(self, theatre_layout, "assets/login_bg.jpg")
      



