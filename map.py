import object


class Map:
    # Class to manage objects of game. Every object get index, which is key to objects access
    def __init__(self):
        self.__object_list = {}
        self.__next_key = 0

    def add_object(self, ob):
        if not isinstance(ob, object.Object):
            raise TypeError("Map getting only Object type objects")

        self.__object_list[self.__next_key] = ob
        self.__next_key += 1
        return self.__next_key - 1

    def del_object(self, key):
        self.__object_list.pop(key)

    def get_object(self, key):
        return self.__object_list[key]

    def update(self, time_difference):
        for key in self.__object_list.keys():
            if type(self.__object_list[key]) == object.MovingObject:
                self.__object_list[key].update_position(time_difference)

    def __len__(self):
        return len(self.__object_list)


if __name__ == "__main__":
    print(__file__, "not executable file")
