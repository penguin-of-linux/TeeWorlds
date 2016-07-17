import unittest
import object


class ObjectTest(unittest.TestCase):

    def test_segment_crossing(self):
        self.assertEquals(object.Object.is_segment_cross((0, 1), (3, 4)), False)
        self.assertEquals(object.Object.is_segment_cross((-5, 5), (-1, 1)), True)
        self.assertEquals(object.Object.is_segment_cross((0, 1), (0, 0.5)), True)
        self.assertEquals(object.Object.is_segment_cross((-100, -50), (100, 100500)), False)
        self.assertEquals(object.Object.is_segment_cross((0, 0), (0, 0)), True)
        self.assertEquals(object.Object.is_segment_cross((-100, -50), (-50, 100)), True)

    def test_crossing(self):
        ob2 = object.Object((0, 0), (10, 10))
        self.assertEquals(ob2.has_crossing(object.Object((0, 0), (0, 0))), True)
        self.assertEquals(ob2.has_crossing(object.Object((-5, 5), (10, 10))), True)
        self.assertEquals(ob2.has_crossing(object.Object((-5, 5), (3, 3))), False)
        self.assertEquals(ob2.has_crossing(object.Object((-5, 5), (5, 5))), True)
        self.assertEquals(ob2.has_crossing(object.Object((-100, 100), (1000, 1000))), True)
        self.assertEquals(ob2.has_crossing(object.Object((-500, 0), (3, 3))), False)
        self.assertEquals(ob2.has_crossing(object.Object((1, -1), (3, 3))), True)

if __name__ == '__main__':
    unittest.main()
