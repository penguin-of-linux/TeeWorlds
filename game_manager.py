import map
import const
import main_window
import threading
import object
import sys
import time


class GameManager():
    """Connect MainWindow with map"""

    @staticmethod
    def init():
        #GameManager.world_time = time.clock()
        GameManager.prev_update_time = time.clock()
        GameManager.moving_keys = list()
        GameManager.static_keys = list()
        GameManager.__map = map.Map()

        GameManager.player = \
            GameManager.get_object(
                GameManager.create_object(
                    object.MovingObject(
                        position=(const.START_PLAYER_POSITION[0], const.START_PLAYER_POSITION[1]))))

        GameManager.update_phisics_timer = threading.Timer(1.0, GameManager.update)
        GameManager.update_screen_timer = threading.Timer(1.0, GameManager.update_screen)
        GameManager.__main_window = main_window.create_main_window()

    @staticmethod
    def create_object(obj):
        key = GameManager.__map.add_object(obj)
        #GameManager.__main_window.add_object(key)
        if isinstance(obj, object.MovingObject):
            GameManager.moving_keys.append(key)
        elif isinstance(obj, object.StaticObject):
            GameManager.static_keys.append(key)
        return key

    @staticmethod
    def get_object(key):
        return GameManager.__map.get_object(key)

    @staticmethod
    def get_all_objects():
        for key in GameManager.moving_keys + GameManager.static_keys:
            yield GameManager.get_object(key)

    @staticmethod
    def update():
        for obj in GameManager.get_all_objects():
            if isinstance(obj, object.MovingObject):
                old_position = obj.get_position()
                obj.update_x_position()
                for key in GameManager.static_keys:
                    if obj.is_crossing(GameManager.get_object(key)):
                        obj.set_position((old_position.x, old_position.y))

                old_position = obj.get_position()
                obj.update_y_position()
                for key in GameManager.static_keys:
                    if obj.is_crossing(GameManager.get_object(key)):
                        obj.set_position((old_position.x, old_position.y))


        GameManager.update_phisics_timer = threading.Timer(const.UPDATE_TIME, GameManager.update)
        GameManager.update_phisics_timer.start()

    @staticmethod
    def update_screen():
        GameManager.__main_window.update()
        GameManager.update_screen_timer = threading.Timer(const.FPS, GameManager.update_screen)
        GameManager.update_screen_timer.start()

    @staticmethod
    def exit():
        GameManager.update_phisics_timer.cancel()
        GameManager.update_screen_timer.cancel()
        GameManager.__main_window.app.closeAllWindows()
        GameManager.__main_window.app.exit(0)
        sys.exit("finished epta")

    @staticmethod
    def start():
        GameManager.__main_window.show()
        GameManager.update_phisics_timer.start()
        GameManager.update_screen_timer.start()
        GameManager.__main_window.app.exec_()