from math import sqrt


if __name__ == "__main__":
    print("it is not executable file")

class Vector2D():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __len__(self):
        return sqrt(self.x * self.x + self.y * self.y)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def normalize(self):
        len = self.__len__()
        return Vector2D(self.x / len, self.y / len) if len != 0 else Vector2D(0, 0)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# segment[0] < segment[1]
def is_segment_cross(segment1, segment2):

    if segment2[0] <= segment1[0] <= segment2[1] or \
        segment2[0] <= segment1[1] <= segment2[1] or \
        segment1[0] <= segment2[0] <= segment1[1] or \
        segment1[0] <= segment2[1] <= segment1[1]:
        return True
    return False