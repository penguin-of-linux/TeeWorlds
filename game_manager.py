import map as Map
import object
import main_window


class GameManager():
    """Connect MainWindow with map"""

    __map = Map.Map()
    __main_window = main_window.MainWindow()

    @staticmethod
    def create_object(obj):
        key = GameManager.__map.add_object(obj)
        GameManager.__main_window.add_object(key)

    @staticmethod
    def set_object_position(key, position):
        """position - (x, y)"""
        GameManager.__map.get_object(key).set_position(position)
        GameManager.__main_window.set_position(key, position)