import sys
import game_manager
import object
import const
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QWidget, QApplication
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt, pyqtSignal

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.setGeometry(0, 0, 1376, 768)

    def paintEvent(self, QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        for obj in game_manager.GameManager.get_all_objects():
            pos = obj.get_position()
            qp.drawRect(pos[0], pos[1], 64, 64)
        qp.end()


    def keyPressEvent(self, event):

        if event.key() == Qt.Key_F:
            print("prost")
            game_manager.GameManager.create_object(object.MovingObject(velocity = (3, 3)))
        if event.key() == Qt.Key_Escape:
            game_manager.GameManager.exit()


def create_main_window():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.app = app
    return main_window
