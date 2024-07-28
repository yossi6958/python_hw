import random


class CrazyPlane:
    def __init__(self):
        self.x = 0
        self.y = 0

    def update_position(self):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)

    def get_position(self):
        return self.x, self.y

    def countdown(self):
        for i in range(10, 0, -1):
            print(i)

    def set_position(self):
        pass


def main():
    plane1 = CrazyPlane()
    x, y = plane1.get_position()


if __name__ == '__main__':
    main()
