import sys
import const
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QWidget, QApplication
from PyQt5.QtGui import QPixmap

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.objects = {}

    def add_object(self, key):
        obj = self.objects[key] = QLabel("", self)
        obj.setPixmap(QPixmap("gimp_gimp.png"))


    def get_object(self, key):
        return self.objects[key]

    def set_object_position(self, key, position):
        self.objects[key].move(position[0], position[1])


def create_main_window():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.app = app
    return main_window
