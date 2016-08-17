import const
from geometry import Vector2D
from geometry import is_segment_cross


class Object:
    '''Class to manipulate all game units'''

    def __init__(self, position=(0, 0), size=(30, 30)):
        self.__position = Vector2D(position[0], position[1])
        self.__size = Vector2D(size[0], size[1])

    def get_position(self):
        """Returns object with x, y fields"""
        return self.__position

    def set_position(self, position):
        if isinstance(position, Vector2D):
            self.__position = position
        else:
            self.__position = Vector2D(position[0], position[1])

    def get_size(self):
        """Returns object with x, y fields"""
        return self.__size

    def set_size(self, size):
        self.__size = Vector2D(size[0], size[1])

    def is_crossing(self, ob):

        # watch crossing for x-axis and y-axis

        x_segment1 = (self.__position.x, self.__position.x + self.__size.x)
        x_segment2 = (ob.__position.x, ob.__position.x + ob.__size.x)

        y_segment1 = (self.__position.y, self.__position.y + self.__size.y)
        y_segment2 = (ob.__position.y, ob.__position.y + ob.__size.y)

        x_axis = is_segment_cross(x_segment1, x_segment2)
        y_axis = is_segment_cross(y_segment1, y_segment2)

        return x_axis and y_axis


class StaticObject(Object):
    def __init__(self, position=(0, 0), size=(30, 30)):
        super().__init__(position, size)


class MovingObject(Object):
    def __init__(self, position=(0, 0), size=(30, 30), velocity=(0, 0)):
        """All paramtres - (x, y)"""

        self.__velocity = Vector2D(velocity[0], velocity[1])
        self.__accelerate = Vector2D(0, const.GRAVITATION)
        self.fixed_velocity = Vector2D()
        super().__init__(position, size)

    def get_velocity(self):
        return self.__velocity

    def set_velocity(self, velocity):
        self.__velocity = Vector2D(velocity[0], velocity[1])

    def get_accelerate(self):
        return self.__accelerate

    def set_accelerate(self, accelerate):
        self.__accelerate = Vector2D(accelerate[0], accelerate[1])

    def add_velocity(self, accelerate):
        """Accept tuple"""
        if self.__velocity.x < const.MAX_SPEED_X and accelerate[0] > 0 or \
                self.__velocity.x > -const.MAX_SPEED_X and accelerate[0] < 0:
            self.__velocity.x += accelerate[0]
        if (self.__velocity.y < const.MAX_SPEED_Y and accelerate[1] > 0) or accelerate[1] < 0:
            self.__velocity.y += accelerate[1]

    def update_x_position(self):
        if self.__velocity.x < 0:
            self.add_velocity((const.RESISTION, 0))
        elif self.__velocity.x > 0:
            self.add_velocity((-const.RESISTION, 0))
        #self.add_velocity((self.__accelerate.x, 0))
        pos = self.get_position()
        self.set_position((pos.x + self.__velocity.x, pos.y))


    def update_y_position(self):
        self.add_velocity((0, self.__accelerate.y))
        pos = self.get_position()
        self.set_position((pos.x, pos.y + self.__velocity.y))


class Bullet(MovingObject):
    def __init__(self, vector:Vector2D, position=(0, 0), size=(5, 5)):
        super().__init__(position=position, size=size)
        self.fixed_velocity = Vector2D(vector.x * const.BULLET_VELOCITY, vector.y * const.BULLET_VELOCITY)

    def update_position(self):
        self.set_position(self.get_position() + self.fixed_velocity)
        
class Unit(MovingObject):
    def __init__(self, position=(0, 0), size=(30, 30), velocity=(0, 0)):
        super().__init__(position=position, size=size, velocity=velocity)


if __name__ == "__main__":
    print(__file__, "not executable file")

