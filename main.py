from game_manager import GameManager
import object
import threading


#if __name__ == "__main__":
GameManager.init()
#key = GameManager.create_object(object.MovingObject())
#GameManager.get_object(key).set_accelerate((1, 1))
GameManager.start()