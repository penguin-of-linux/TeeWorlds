import sys
import game_manager
import object
import random
from const import TILE_LENGHT, START_PLAYER_POSITION, JUMP_VELOCITY, MOVE_VELOCITY, BULLET_VELOCITY
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QWidget, QApplication
from PyQt5.QtGui import QPixmap, QPainter, QColor, QImage
from PyQt5.QtCore import Qt, pyqtSignal
from geometry import Vector2D


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.images = {}
        self.setGeometry(0, 0, 1376, 768)

    def paintEvent(self, QPaintEvent):
        qp = QPainter()
        image = QImage("default.png")
        image = image.scaled(32, 32)
        sky_image = QImage("sky.png")
        qp.begin(self)
        qp.drawImage(0, 0, sky_image)
        for obj in game_manager.GameManager.get_all_objects():
            pos = obj.get_position()
            size = obj.get_size()
            #if isinstance(obj, object.MovingObject):
                #qp.setPen(QColor(0, 0, 0))
            #else:
                #qp.setPen(QColor(255, 0, 0))
            if obj is object.Bullet:
                pass
            if isinstance(obj, object.Unit):
                qp.drawImage(pos.x + START_PLAYER_POSITION[0] - game_manager.GameManager.player.get_position().x,
                         pos.y + START_PLAYER_POSITION[1] - game_manager.GameManager.player.get_position().y,
                         image)
            else:
                qp.drawRect(pos.x + START_PLAYER_POSITION[0] - game_manager.GameManager.player.get_position().x,
                pos.y + START_PLAYER_POSITION[1] - game_manager.GameManager.player.get_position().y,
                size.x, size.y)
        #qp.setPen(QColor(255, 0, 0))
        #for x in game_manager.GameManager.get_map().grid.keys():
            #for y in game_manager.GameManager.get_map().grid[x].keys():
                #qp.drawRect(x + START_PLAYER_POSITION[0] - game_manager.GameManager.player.get_position().x,
                            #y + START_PLAYER_POSITION[1] - game_manager.GameManager.player.get_position().y,
                            #TILE_LENGHT, TILE_LENGHT)
        qp.end()


    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_F:
            game_manager.GameManager.create_object(object.Unit(velocity=(0, 0), position=(random.randint(0, 1376), 0)))
        if key == Qt.Key_Escape:
            game_manager.GameManager.exit()
        if key == Qt.Key_Space:
            game_manager.GameManager.player.add_velocity((0, JUMP_VELOCITY))
        if key == Qt.Key_Left:
            game_manager.GameManager.player.fixed_velocity += Vector2D(-MOVE_VELOCITY, 0)
        if key == Qt.Key_Right:
            game_manager.GameManager.player.fixed_velocity += Vector2D(MOVE_VELOCITY, 0)

    def keyReleaseEvent(self, event):
        key = event.key()
        if key == Qt.Key_Right:
            game_manager.GameManager.player.fixed_velocity += Vector2D(-MOVE_VELOCITY, 0)
        if key == Qt.Key_Left:
            game_manager.GameManager.player.fixed_velocity += Vector2D(MOVE_VELOCITY, 0)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            player_pos = game_manager.GameManager.player.get_position()
            vector = Vector2D(event.x() - player_pos.x, event.y() - player_pos.y).normalize()
            game_manager.GameManager.create_object(object.Bullet(vector=vector, position=(player_pos.x, player_pos.y)))


def create_main_window():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.app = app
    return main_window
