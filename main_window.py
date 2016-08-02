import sys
import game_manager
import object
import random
import const
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QWidget, QApplication
from PyQt5.QtGui import QPixmap, QPainter, QColor
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
            size = obj.get_size()
            if isinstance(obj, object.MovingObject):
                qp.setPen(QColor(0, 0, 0))
            else:
                qp.setPen(QColor(255, 0, 0))
            qp.drawRect(pos.x + const.START_PLAYER_POSITION[0] - game_manager.GameManager.player.get_position().x,
                        pos.y + const.START_PLAYER_POSITION[1] - game_manager.GameManager.player.get_position().y,
                        size.x, size.y)
        qp.end()


    def keyPressEvent(self, event):

        if event.key() == Qt.Key_F:
            game_manager.GameManager.create_object(object.MovingObject(velocity=(0, 0), position=(random.randint(0, 1376), 0)))
        if event.key() == Qt.Key_Escape:
            game_manager.GameManager.exit()
        if event.key() == Qt.Key_Space:
            game_manager.GameManager.player.set_velocity((game_manager.GameManager.player.get_velocity().x, -8))#magic numbers
        if event.key() == Qt.Key_Left:
            game_manager.GameManager.player.set_velocity((-2, game_manager.GameManager.player.get_velocity().y))
        if event.key() == Qt.Key_Right:
            game_manager.GameManager.player.set_velocity((2, game_manager.GameManager.player.get_velocity().y))


def create_main_window():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.app = app
    return main_window
