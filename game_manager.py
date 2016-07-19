import map
import object
import main_window
import threading


class GameManager():
    """Connect MainWindow with map"""

    @staticmethod
    def init():
        GameManager.keys = list()
        GameManager.__map = map.Map()
        GameManager.update_timer = threading.Timer(1.0, GameManager.update)
        GameManager.update_timer.start()
        GameManager.__main_window = main_window.create_main_window()

    @staticmethod
    def create_object(obj):
        key = GameManager.__map.add_object(obj)
        GameManager.__main_window.add_object(key)
        GameManager.keys.append(key)
        return key

    @staticmethod
    def set_object_position(key, position):
        """position - (x, y)"""
        GameManager.__map.get_object(key).set_position(position)
        GameManager.__main_window.set_object_position(key, position)

    @staticmethod
    def get_object(key):
        return GameManager.__map.get_object(key)

    @staticmethod
    def update():
        print("Update")
        for key in GameManager.keys:
            GameManager.__main_window.set_object_position(key,
            GameManager.__map.get_object(key).update_position())

        GameManager.update_timer = threading.Timer(1.0, GameManager.update)
        GameManager.update_timer.start()

    @staticmethod
    def start():
        GameManager.__main_window.show()
        GameManager.__main_window.app.exec_()