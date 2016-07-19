from game_manager import GameManager
import object


#if __name__ == "__main__":
GameManager.init()
key = GameManager.create_object(object.MovingObject())
GameManager.set_object_position(key, (30, 100))
GameManager.get_object(key).set_velocity((5, 5))
GameManager.start()