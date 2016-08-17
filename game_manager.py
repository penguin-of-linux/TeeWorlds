import const
import threading
import sys
import time

from main_window import MainWindow, create_main_window
from map import Map
from object import Object, MovingObject, StaticObject, Unit, Bullet


class GameManager():
    """Connect MainWindow with map"""

    @staticmethod
    def init():
        #GameManager.world_time = time.clock()
        GameManager.prev_update_time = time.clock()
        GameManager.unit_keys = list()
        GameManager.static_keys = list()
        GameManager.bullet_keys = list()
        GameManager.__map = Map()
        #GameManager.__map.load_map()

        GameManager.player = \
            GameManager.get_object(
                GameManager.create_object(
                    Unit(
                        position=(const.START_PLAYER_POSITION[0], const.START_PLAYER_POSITION[1]))))

        GameManager.update_phisics_timer = threading.Timer(1.0, GameManager.update)
        GameManager.update_screen_timer = threading.Timer(1.0, GameManager.update_screen)
        GameManager.__main_window = create_main_window()

    @staticmethod
    def get_map():
        return GameManager.__map

    @staticmethod
    def create_object(obj):
        key = GameManager.__map.add_object(obj)
        if isinstance(obj, Unit):
            GameManager.unit_keys.append(key)
        elif isinstance(obj, StaticObject):
            GameManager.static_keys.append(key)
        elif isinstance(obj, Bullet):
            GameManager.bullet_keys.append(key)

        return key

    @staticmethod
    def get_object(key):
        return GameManager.__map.get_object(key)

    @staticmethod
    def get_all_static_objects():
        for key in GameManager.static_keys:
            yield GameManager.get_object(key)

    @staticmethod
    def get_all_units():
        for key in GameManager.unit_keys:
            yield GameManager.get_object(key)

    @staticmethod
    def get_all_objects():
        for key in GameManager.unit_keys + GameManager.static_keys + GameManager.bullet_keys:
            yield GameManager.get_object(key)

    @staticmethod
    def update():
        GameManager.player.add_velocity((GameManager.player.fixed_velocity.x, GameManager.player.fixed_velocity.y))
        for obj in GameManager.get_all_units():
            obj.update_x_position()
            obj_pos = obj.get_position()
            for stc_obj in GameManager.get_all_static_objects():
                if obj.is_crossing(stc_obj):
                    stc_obj_pos = stc_obj.get_position()
                    if stc_obj_pos.x >= obj_pos.x:
                        obj.set_position(
                            (obj_pos.x - (obj_pos.x + obj.get_size().x - stc_obj_pos.x) - 1, obj_pos.y))
                    else:
                        obj.set_position(
                            (obj_pos.x + (stc_obj_pos.x + stc_obj.get_size().x - obj_pos.x) + 1, obj_pos.y))

            obj.update_y_position()
            for stc_obj in GameManager.get_all_static_objects():
                if obj.is_crossing(stc_obj):
                    obj_pos = obj.get_position()
                    stc_obj_pos = stc_obj.get_position()
                    if stc_obj_pos.y > obj_pos.y:
                        obj.set_position((obj_pos.x, obj_pos.y - (obj_pos.y + obj.get_size().y - stc_obj_pos.y) - 1))
                    elif stc_obj_pos.y < obj_pos.y:
                        obj.set_position((obj_pos.x, obj_pos.y + (stc_obj_pos.y + stc_obj.get_size().y - obj_pos.y) + 1))
        for key in GameManager.bullet_keys:
            GameManager.get_object(key).update_position()
            #GameManager.get_object(key).update_x_position()
            #GameManager.get_object(key).update_y_position()

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