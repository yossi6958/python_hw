from BigThing import BigThing


class BigCat(BigThing):
    def __init__(self, var, weight):
        super(BigCat, self).__init__(var)
        self.__weight = weight

    def size(self):
        if self.__weight > 20:
            return "Very Fat"
        elif self.__weight > 15:
            return "Fat"
        else:
            return "OK"
