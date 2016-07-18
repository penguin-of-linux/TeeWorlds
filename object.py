
class Object:
    '''Class to manipulate all game units'''
    @staticmethod
    def is_pair_type(value):
        if type(value) == tuple and len(value) > 1:
            return True
        return False

    @staticmethod
    # segment[0] > segment[1]
    def is_segment_cross(segment1, segment2):

        if segment2[0] <= segment1[0] <= segment2[1] or \
           segment2[0] <= segment1[1] <= segment2[1] or \
           segment1[0] <= segment2[0] <= segment1[1] or \
           segment1[0] <= segment2[1] <= segment1[1]:
            return True
        return False

    def __init__(self, cords=(0, 0), size=(0, 0)):
        if not Object.is_pair_type(cords):
            self.__cords = (0, 0)
            raise TypeError("cords parameter should have type tuple with size = 2 at least")

        if not Object.is_pair_type(size):
            self.__size = (0, 0)
            raise TypeError("size parameter should have type tuple with size = 2 at least")

        self.__cords = cords
        self.__size = size

    def get_cords(self):
        return self.__cords

    def set_cords(self, cords):
        if not Object.is_pair_type(cords):
            raise TypeError("cords parameter should have type tuple with size = 2 at least")
        self.__cords = cords

    def get_size(self):
        return self.__size

    def set_size(self, size):
        if not Object.is_pair_type(size):
            raise TypeError("size parameter should have type tuple with size = 2 at least")
        self.__size = size

    def has_crossing(self, ob):
        if not isinstance(ob, Object):
            raise TypeError("ob parameter should have type Object")

        # watch crossing for x-axis and y-axis

        x_segment1 = (self.__cords[0], self.__cords[0] + self.__size[0])
        x_segment2 = (ob.__cords[0], ob.__cords[0] + ob.__size[0])

        y_segment1 = (self.__cords[1] - self.__size[1], self.__cords[1])
        y_segment2 = (ob.__cords[1] - ob.__size[1], ob.__cords[1])

        x_axis = Object.is_segment_cross(x_segment1, x_segment2)
        y_axis = Object.is_segment_cross(y_segment1, y_segment2)

        return x_axis and y_axis


class StaticObject(Object):
    def __init__(self, cords=(0, 0), size=(0, 0)):
        Object.__init__(cords, size)


class MovingObject(Object):
    def __init__(self, cords=(0, 0), size=(0, 0), velocity=(0, 0), accelerate=(0, 0)):
        if not Object.is_pair_type(velocity):
            self.__velocity = (0, 0)
            raise TypeError("velocity parameter should have tuple type with size = 2 at least")

        if not Object.is_pair_type(accelerate):
            self.__accelerate = (0, 0)
            raise TypeError("accelerate parameter should have tuple type with size = 2 at least")

        self.__velocity = velocity
        self.__accelerate = accelerate
        Object.__init__(self, cords, size)

    def get_velocity(self):
        return self.__velocity

    def set_velocity(self, velocity):
        if not Object.is_pair_type(velocity):
            raise TypeError("velocity parameter should have tuple type with size = 2")
        self.__velocity = velocity

    def get_accelerate(self):
        return self.__accelerate

    def set_accelerate(self, accelerate):
        if not Object.is_pair_type(accelerate):
            raise TypeError("accelerate parameter should have tuple type with size = 2")

        self.__accelerate = accelerate

    def update(self, time_difference):
        self.__velocity[0] += self.__accelerate[0] * time_difference
        self.__velocity[1] += self.__accelerate[1] * time_difference

        self.__cords[0] += self.__velocity[0] * time_difference
        self.__cords[1] += self.__velocity[1] * time_difference


if __name__ == "__main__":
    print(__file__, "not executable file")
    
