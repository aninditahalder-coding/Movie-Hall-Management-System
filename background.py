from PySide6.QtWidgets import QLabel,QWidget,QStackedLayout,QGraphicsBlurEffect
from PySide6.QtGui import QPixmap

#set stylsheet

HEADING_STYLE = """
    font-size: 44px;
    font-weight: bold;
    color: white;
    background: rgba(0, 0, 0, 120);
    padding: 14px;
    border-radius: 6px;
"""


# style for buttons (Browse Movies, Exit, Select Movie, INOX/SVF, showtimes, etc.)

BUTTON_STYLE = """
    QPushButton {
        font-size: 20px;
        font-weight: 600;
        padding: 10px 16px;
        border-radius: 6px;
    }
"""

# style for regular body text labels (movie names, ratings, show-time label, etc.)

LABEL_STYLE = """
    font-size: 18px;
    font-weight: 500;
    color: white;
"""

#background image blur

def apply_blur_background(window, content_layout,image_path, blur_radius=10):
    #background label holding the image,sized to fill the whole window

    background_label=QLabel(window)
    pixmap=QPixmap(image_path)
    background_label.setPixmap(pixmap)
    background_label.setScaledContents(True)

    #blur effect allocated to the background only

    blur_effect=QGraphicsBlurEffect()
    blur_effect.setBlurRadius(blur_radius)
    background_label.setGraphicsEffect(blur_effect)

    # wrap the existing content layout in a transparent widget so it sits visually on top of the blurred background image

    content_widget=QWidget()
    content_widget.setLayout(content_layout)
    content_widget.setStyleSheet("background: transparent;")

    # stack the background and content widgets on top of each other, both filling the full window

    stacked_layout=QStackedLayout()
    stacked_layout.setStackingMode(QStackedLayout.StackAll)
    stacked_layout.addWidget(background_label)
    stacked_layout.addWidget(content_widget)
 
    window.setLayout(stacked_layout)
 
    # keep a reference so it doesn't get garbage collected
 
    window.background_label = background_label
 
    return stacked_layout


