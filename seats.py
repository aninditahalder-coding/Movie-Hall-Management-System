from PySide6.QtWidgets import(QLabel,QWidget,QPushButton,QVBoxLayout,QGridLayout)
from PySide6.QtCore import Qt
from background import apply_blur_background,BUTTON_STYLE,LABEL_STYLE

rows='ABCDEF'
cols=8

class seat_window(QWidget):
    def __init__(self):
        super(). __init__()
        self.setWindowTitle("Seat Selection")
        # ---- data structures ----
        # 2D matrix: each row is a list of seat ids like "A1", "A2", ...
        self.seat_matrix=[[f"{r}{c}" for c in range(1, cols+1)]for r in rows]
        # set: fast membership check (sample data for now, from the database later)
        self.booked_seats = {"A3", "A4", "C5", "D1", "D2"}
        # list: seats the user has picked right now
        self.selected_seats = []
        # seat id -> button, so we can restyle it later
        self.seat_buttons = {}

        #heading----

        self.title=QLabel("Choose Your View!!")
        self.title.setStyleSheet("""
            font-family: 'Georgia', 'Times New Roman', serif;
            font-size: 40px; font-weight: 900; font-style: italic;
            color: #FFD700; padding: 8px;
         """)
        self.title.setAlignment(Qt.AlignLeft)


        # ---- movie | theatre | time line ----
        self.info_label = QLabel("")
        self.info_label.setStyleSheet(LABEL_STYLE)

        self.screen_label = QLabel("SCREEN THIS WAY")
        self.screen_label.setStyleSheet("""
            background: rgba(255, 255, 255, 180); color: black;
            font-size: 18px; font-weight: bold; padding: 8px;
            border-radius: 6px;
        """)

        #seat Grid

        grid=QGridLayout()
        grid.setSpacing(8)
        for r, row in enumerate(self.seat_matrix):
            for c,seat_id in enumerate(row):
                btn=QPushButton(seat_id)
                btn.setFixedSize(60,45)
                self.seat_buttons[seat_id]=btn
                self.update_seat_style(seat_id)
                if seat_id in self.booked_seats:
                    btn.setEnabled(False)
                else:
                    btn.clicked.connect(lambda checked=False, s=seat_id: self.toggle_seat(s))
                
                #gap for aisle

                grid_col=c if c < 5 else c+1
                grid.addWidget(btn,r,grid_col)
                grid.setColumnMinimumWidth(5,40)
        #summary+ buttons

        self.summary_label=QLabel("Selected Seats : None")
        self.summary_label.setStyleSheet(LABEL_STYLE)

        self.confirm_button=QPushButton("Confirm Booking")
        self.back_button=QPushButton("Back to Theatres")
        for b in(self.confirm_button, self.back_button):
            b.setStyleSheet(BUTTON_STYLE)

        #main layout

        layout=QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.info_label)
        layout.addWidget(self.screen_label)
        layout.addLayout(grid)
        layout.addWidget(self.summary_label)
        layout.addWidget(self.confirm_button)
        layout.addWidget(self.back_button)

        apply_blur_background(self,layout,"assets/login_bg.jpg")

    #for setting the details

    def set_details(self, movie, theatre, time):
        self.info_label.setText(f"{movie}  |  {theatre}  |  {time}")
        self.selected_seats.clear()
        for seat_id in self.seat_buttons:
            self.update_seat_style(seat_id)
        self.update_summary()

    #for selecting the seats  


    def toggle_seat(self, seat_id):
        if seat_id in self.selected_seats:
            self.selected_seats.remove(seat_id)
        else:
            self.selected_seats.append(seat_id)
        self.update_seat_style(seat_id)
        self.update_summary()

     #for updating the seats colour    


    def update_seat_style(self, seat_id):
        btn = self.seat_buttons[seat_id]
        if seat_id in self.booked_seats:
            color, text = "#555555", "#999999"      # booked = gray
        elif seat_id in self.selected_seats:
            color, text = "#FFD700", "black"        # selected = gold
        else:
            color, text = "#2E8B57", "white"        # available = green
        btn.setStyleSheet(
            f"background: {color}; color: {text}; font-weight: bold; border-radius: 6px;"
        )


    def update_summary(self):
        if self.selected_seats:
            self.summary_label.setText("Selected seats: " + ", ".join(self.selected_seats))
        else:
            self.summary_label.setText("Selected seats: None")

    #for confirm booking
    def confirm_booking(self):
        if not self.selected_seats:
            self.summary_label.setText("Please select at least one seat!!!!")
            return None
        confirmed=list(self.selected_seats)
        self.booked_seats.update(confirmed)


        self.selected_seats.clear()
        for seat_id in confirmed:
            self.update_seat_style(seat_id)
        self.update_summary()
 
        return confirmed
        









        

    