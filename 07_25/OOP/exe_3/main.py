import random


class CrazyPlane:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def update_position(self):
        self.__x += random.randint(-1, 1)
        self.__y += random.randint(-1, 1)

    def get_position(self):
        return self.__x, self.__y

    def countdown(self):
        for i in range(10, 0, -1):
            print(i)

    def set_position(self):
        pass


def main():
    plane1 = CrazyPlane(5, 5, )
    x, y = plane1.get_position()


if __name__ == '__main__':
    main()
