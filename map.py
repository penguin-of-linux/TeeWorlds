from object import Object, MovingObject
from const import TILE_LENGHT
from geometry import Vector2D


class Map:
    # Class to manage objects of game. Every object get index, which is key to objects access
    def __init__(self):
        self.__object_list = {}
        self.__next_key = 0
        self.grid = {}

    def load_map(self, file=None):
        if file is None:
            self.grid[320] = {}
            #for i in range(0, 1000*TILE_LENGHT, TILE_LENGHT):
                #self.grid[320][i] = 1
            for i in range(0, 1000 * TILE_LENGHT, TILE_LENGHT):
                self.grid[i] = {}
                self.grid[i][640] = 1
        else:
            pass

    def add_object(self, ob:Object):

        self.__object_list[self.__next_key] = ob
        self.__next_key += 1
        return self.__next_key - 1

    def del_object(self, key):
        self.__object_list.pop(key)

    def get_object(self, key):
        return self.__object_list[key]

    def get_nearest_x_tile(self, obj : MovingObject):
        """returns position as tuple"""
        pos = obj.get_position()
        vel = obj.get_velocity()
        size = obj.get_size()
        tiles = Vector2D()
        result = []
        if vel.x > 0:
            tiles.x = pos.x + size.x - (pos.x + size.x) % TILE_LENGHT + TILE_LENGHT
        elif vel.x < 0:
            tiles.x = pos.x + size.x - pos.x % TILE_LENGHT - TILE_LENGHT
        else:
            return []
        for i in range(pos.y - pos.y % TILE_LENGHT, (pos.y + size.y) + (pos.y + size.y) % TILE_LENGHT, TILE_LENGHT):
            result.append(Object(position=(tiles.x, i), size=(TILE_LENGHT, TILE_LENGHT)))
        return result

    def get_nearest_y_tile(self, obj : MovingObject):
        """returns position as tuple"""
        pos = obj.get_position()
        vel = obj.get_velocity()
        size = obj.get_size()
        tiles = Vector2D()
        result = []
        if vel.y > 0:
            tiles.y = pos.y + size.y - (pos.y + size.y) % TILE_LENGHT + TILE_LENGHT
        elif vel.y < 0:
            tiles.y = pos.y + size.y - pos.y % TILE_LENGHT - TILE_LENGHT
        else:
            return []
        for i in range(pos.x - pos.x % TILE_LENGHT, (pos.x + size.x) + (pos.x + size.x) % TILE_LENGHT, TILE_LENGHT):
            result.append(Object(position=(i, tiles.y), size=(TILE_LENGHT, TILE_LENGHT)))
        return result

    def __len__(self):
        return len(self.__object_list)


if __name__ == "__main__":
    print(__file__, "not executable file")
