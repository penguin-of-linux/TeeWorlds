import unittest
from map import Map
from object import MovingObject, Object
from const import TILE_LENGHT


class MapTest(unittest.TestCase):

    def test_get_nearest_tile(self):
        obj = MovingObject(position=(42, 42), size=(TILE_LENGHT, TILE_LENGHT), velocity=(1, 1))
        map = Map()
        map.grid = {}
        for i in range(0, 100*TILE_LENGHT, TILE_LENGHT):
            map.grid[i] = {}
            map.grid[i][0] = 1
        right_result = []
        right_result.append(Object(position=(TILE_LENGHT * 3, TILE_LENGHT)))
        right_result.append(Object(position=(TILE_LENGHT * 3, TILE_LENGHT * 2)))
        result = map.get_nearest_x_tile(obj)
        for i in range(0, result.__len__(), 1):
            a = result[i].get_position()
            b = right_result[i].get_position()
            self.assertEqual(a, b)

        right_result = []
        right_result.append(Object(position=(TILE_LENGHT, TILE_LENGHT * 3)))
        right_result.append(Object(position=(TILE_LENGHT * 2, TILE_LENGHT * 3)))
        result = map.get_nearest_y_tile(obj)
        for i in range(0, result.__len__(), 1):
            a = result[i].get_position()
            b = right_result[i].get_position()
            self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()
