class BigThing:
    def __init__(self, var):
        self.__var = var

    def size(self):
        if type(self.__var) is int:
            return self.__var
        elif type(self.__var) in [list, dict, str]:
            return len(self.__var)
