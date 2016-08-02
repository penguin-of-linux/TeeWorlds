import const


class Object:
    '''Class to manipulate all game units'''

    @staticmethod
    # segment[0] < segment[1]
    def is_segment_cross(segment1, segment2):

        if segment2[0] <= segment1[0] <= segment2[1] or \
           segment2[0] <= segment1[1] <= segment2[1] or \
           segment1[0] <= segment2[0] <= segment1[1] or \
           segment1[0] <= segment2[1] <= segment1[1]:
            return True
        return False

    def __init__(self, position=(0, 0), size=(30, 30)):
        self.__position = Point(position[0], position[1])
        self.__size = Point(size[0], size[1])

    def get_position(self):
        """Returns object with x, y fields"""
        return self.__position

    def set_position(self, position):
        self.__position = Point(position[0], position[1])

    def get_size(self):
        """Returns object with x, y fields"""
        return self.__size

    def set_size(self, size):
        self.__size = Point(size[0], size[1])

    def is_crossing(self, ob):
        if not isinstance(ob, Object):
            raise TypeError("ob parameter should have type Object")

        # watch crossing for x-axis and y-axis

        x_segment1 = (self.__position.x, self.__position.x + self.__size.x)
        x_segment2 = (ob.__position.x, ob.__position.x + ob.__size.x)

        y_segment1 = (self.__position.y, self.__position.y + self.__size.y)
        y_segment2 = (ob.__position.y, ob.__position.y + ob.__size.y)

        x_axis = Object.is_segment_cross(x_segment1, x_segment2)
        y_axis = Object.is_segment_cross(y_segment1, y_segment2)

        return x_axis and y_axis


class StaticObject(Object):
    def __init__(self, position=(0, 0), size=(30, 30)):
        super().__init__(position, size)


class MovingObject(Object):
    def __init__(self, position=(0, 0), size=(30, 30), velocity=(0, 0)):
        """All paramtres - (x, y)"""

        self.__velocity = Point(velocity[0], velocity[1])
        self.__accelerate = Point(0, const.GRAVITATION)
        super().__init__(position, size)

    def get_velocity(self):
        return self.__velocity

    def set_velocity(self, velocity):
        self.__velocity = Point(velocity[0], velocity[1])

    def get_accelerate(self):
        return self.__accelerate

    def set_accelerate(self, accelerate):
        self.__accelerate = Point(accelerate[0], accelerate[1])


    def update_x_position(self):
        if self.__velocity.x < const.MAX_SPEED_X:
            self.__velocity.x += self.__accelerate.x
        pos = self.get_position()
        self.set_position((pos.x + self.__velocity.x, pos.y))

    def update_y_position(self):
        if self.__velocity.y < const.MAX_SPEED_Y:
            self.__velocity.y += self.__accelerate.y
        pos = self.get_position()
        self.set_position((pos.x, pos.y + self.__velocity.y))


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    print(__file__, "not executable file")

