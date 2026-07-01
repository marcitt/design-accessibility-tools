"""
boilerplate for pyqt accessibility overlays 
very minimal implementation
"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtCore import Qt, QTimer

import pyautogui

SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()


class Overlay(QWidget):
    def __init__(self):
        super().__init__() #think a little more about what super means

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground) #makes background transparent
        self.setAttribute(Qt.WA_TransparentForMouseEvents) #theoretically enables click-through
        
        # self.showFullScreen() doesn't usually work as expected
        self.setGeometry(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

        self.show()
        
        # Example rectangles (x, y, w, h)
        self.rects = [(100, 100, 200, 100), (400, 300, 150, 150)]

        # Trigger redraw approx 30 FPS - may not allways be required
        # QTimer(self, timeout=self.update).start(33)


    def paintEvent(self, _):
        p = QPainter(self)
        for x, y, w, h in self.rects:
            p.drawRect(x, y, w, h)
            
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()
            sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = Overlay()
    sys.exit(app.exec())