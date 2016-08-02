from game_manager import GameManager
import object
import threading


#if __name__ == "__main__":
GameManager.init()
#key = GameManager.create_object(object.MovingObject())
#GameManager.get_object(key).set_accelerate((1, 1))
GameManager.create_object(object.StaticObject(position=(300, 300), size=(300, 300)))
#GameManager.create_object((object.MovingObject(position=(100, 100), size=(100, 50))))
GameManager.start()