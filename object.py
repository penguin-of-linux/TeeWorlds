
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

    def __init__(self, cords, size):
        if not Object.is_pair_type(cords):
            self.__cords = (0, 0)
            raise TypeError("cords parameter should have type tuple with size 2")

        if not Object.is_pair_type(size):
            self.__size = (0, 0)
            raise TypeError("size parameter should have type tuple with size 2")

        self.__cords = cords
        self.__size = size

    def get_cords(self):
        return self.__cords

    def set_cords(self, cords):
        if not Object.is_pair_type(cords):
            raise TypeError("cords parameter should have type tuple with size 2")
        self.__cords = cords

    def get_size(self):
        return self.__size

    def set_size(self, size):
        if not Object.is_pair_type(size):
            raise TypeError("size parameter should have type tuple with size 2")
        self.__size = size

    def has_crossing(self, ob):
        if type(ob) != Object:
            raise TypeError("ob parameter should have type Object")

        # watch crossing for x-axis and y-axis

        x_segment1 = (self.__cords[0], self.__cords[0] + self.__size[0])
        x_segment2 = (ob.__cords[0], ob.__cords[0] + ob.__size[0])

        y_segment1 = (self.__cords[1] - self.__size[1], self.__cords[1])
        y_segment2 = ( ob.__cords[1] - ob.__size[1], ob.__cords[1])

        x_axis = Object.is_segment_cross(x_segment1, x_segment2)
        y_axis = Object.is_segment_cross(y_segment1, y_segment2)

        return x_axis and y_axis



if __name__ == "__main__":
    print("Should not run this file")
    ob = Object((1, 1), (5, 5))
    print(ob.has_crossing(Object((4, 4), (10, 10))))
