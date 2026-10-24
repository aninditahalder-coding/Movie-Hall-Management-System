import sys
from PySide6.QtWidgets import( QApplication,QWidget, QLabel, QPushButton,QVBoxLayout,QHBoxLayout,QDialog)
from home import HomeWindow
from movies import MoviesWindow
from theatre import theatrewindow
from login import loginWindow
from seats import seat_window
from confirmation import confirmation_window
from movie_details import movie_details_window
from bookings import my_bookings_window
from registration import sign_up_window
from profile import profile_window



#create application

app=QApplication(sys.argv)
#all win0dows

home_window=HomeWindow()
movies_window=MoviesWindow()
theatre_window=theatrewindow()
seats_window =seat_window()
confirmation_win= confirmation_window()
details_win = movie_details_window()
login_window=loginWindow()
signup_window = sign_up_window()
bookings_window=my_bookings_window()
profile_win = profile_window()


# booking history, and who is currently logged in

all_bookings = []
current_user = {"username": None}


#what the user has selected so far

booking= {"movie": None, "theatre": None, "time": None}


#confirm booking and show my bookinbgs

def handle_confirm():
    confirmed_seats = seats_window.confirm_booking()
    if not confirmed_seats:
        return
    booking_entry = {
        "movie": booking["movie"],
        "theatre": booking["theatre"],
        "time": booking["time"],
        "seats": confirmed_seats,
        "total": len(confirmed_seats) * 250  # example pricing
    }
    all_bookings.append(booking_entry)

    confirmation_win.set_booking(
        booking["movie"], booking["theatre"], booking["time"], confirmed_seats
    )
    seats_window.hide()
    confirmation_win.showMaximized()



def pick_movie(name):
    booking["movie"] = name
    booking["theatre"] = None      # start fresh for every new movie
    booking["time"] = None
    details_win.set_movie(name)
    movies_window.hide()
    details_win.showMaximized()

def pick_theatre(name):
    booking["theatre"]=name

def go_to_seats(time):
    if booking["theatre"] is None:  # ignore the click until a theatre is chosen
        return
    booking["time"] = time
    theatre_window.hide()
    seats_window.set_details(booking["movie"], booking["theatre"], booking["time"])
    seats_window.showMaximized()

def open_my_bookings():
    my_bookings_win.set_bookings(all_bookings)
    home_window.hide()
    my_bookings_win.showMaximized()


# ---- profile screen ----
 
def open_profile():
    profile_win.set_profile(current_user["username"], all_bookings)
    home_window.hide()
    profile_win.showMaximized()
 
 
def open_signup():
    login_window.hide()
    signup_window.show()


def on_signup_accepted():
    signup_window.hide()
    login_window.status_label.setStyleSheet(
        "color: #5cb85c; font-size: 14px; background: transparent;")
    login_window.status_label.setText("Account created! Please log in.")
    login_window.username_input.clear()
    login_window.password_input.clear()
    login_window.showMaximized()


def on_signup_rejected():
    signup_window.hide()
    login_window.showMaximized()


def on_login_accepted():
    current_user["username"] = login_window.logged_in_username
    login_window.hide()
    home_window.showMaximized()


# login to sign up, and back

login_window.signup_link.clicked.connect(open_signup)
signup_window.accepted.connect(on_signup_accepted)
signup_window.rejected.connect(on_signup_rejected)

# login success -> home

login_window.accepted.connect(on_login_accepted)
login_window.rejected.connect(app.quit)

# home to profile
 
home_window.profile_button.clicked.connect(open_profile)

# profile back to home
 
profile_win.back_button.clicked.connect(profile_win.hide)
profile_win.back_button.clicked.connect(home_window.showMaximized)
 


#home to movies

home_window.browse_button.clicked.connect(home_window.hide)
home_window.browse_button.clicked.connect(movies_window.showMaximized)

#movies to home

movies_window.back_button.clicked.connect(movies_window.hide)
movies_window.back_button.clicked.connect(home_window.showMaximized)

#movieas to movie details

movies_window.select_movie1.clicked.connect(lambda: pick_movie("Avengers"))
movies_window.select_movie2.clicked.connect(lambda: pick_movie("Frozen"))
movies_window.select_movie3.clicked.connect(lambda: pick_movie("Parasite"))
movies_window.select_movie4.clicked.connect(lambda: pick_movie("Interstellar"))

#movie details to movies

details_win.back_button.clicked.connect(details_win.hide)
details_win.back_button.clicked.connect(movies_window.showMaximized)

# movie details to theatre
 
details_win.book_button.clicked.connect(details_win.hide)
details_win.book_button.clicked.connect(theatre_window.showMaximized)


# theatre choice
 
theatre_window.theatre1.clicked.connect(lambda: pick_theatre("Screen 1"))
theatre_window.theatre2.clicked.connect(lambda: pick_theatre("Screen 2"))
theatre_window.theatre3.clicked.connect(lambda: pick_theatre("Screen 3"))
theatre_window.theatre4.clicked.connect(lambda: pick_theatre("Screen 4"))
theatre_window.theatre5.clicked.connect(lambda: pick_theatre("Screen 5"))
 
# showtime choice (opens the seat screen)
 
theatre_window.show1.clicked.connect(lambda: go_to_seats("10:00 AM"))
theatre_window.show2.clicked.connect(lambda: go_to_seats("2:00 PM"))
theatre_window.show3.clicked.connect(lambda: go_to_seats("5:00 PM"))
theatre_window.show4.clicked.connect(lambda: go_to_seats("8:00 PM"))
theatre_window.show5.clicked.connect(lambda: go_to_seats("11:00 AM"))

#theatre to movies

theatre_window.theatre_back.clicked.connect(theatre_window.hide)
theatre_window.theatre_back.clicked.connect(movies_window.showMaximized)

#seats to theatre
 
seats_window.back_button.clicked.connect(seats_window.hide)
seats_window.back_button.clicked.connect(theatre_window.showMaximized)

#seats confoirm buttyon

seats_window.confirm_button.clicked.connect(handle_confirm)

# confirmation screen back to home
 
confirmation_win.done_button.clicked.connect(confirmation_win.hide)
confirmation_win.done_button.clicked.connect(home_window.showMaximized)

# home to bookings
home_window.booking_button.clicked.connect(home_window.hide)
home_window.booking_button.clicked.connect(lambda: bookings_window.set_bookings(all_bookings))
home_window.booking_button.clicked.connect(bookings_window.showMaximized)

# bookings back to home
bookings_window.back_button.clicked.connect(bookings_window.hide)
bookings_window.back_button.clicked.connect(home_window.showMaximized)

# login to sign up, and back
 
login_window.signup_link.clicked.connect(open_signup)


#exit application

home_window.exit_button.clicked.connect(app.quit)


#show login dialog box first and then proceed to home window

login_window.show()
sys.exit(app.exec())