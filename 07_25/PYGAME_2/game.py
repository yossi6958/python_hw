import random

import pygame


class Plane:
    def __init__(self, x, y, color=(0, 255, 0)):
        self.x = x
        self.y = y
        self.color = color
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.direction = random.choice(self.directions)

    def move(self, grid_size):
        new_x = self.x + self.direction[0]
        new_y = self.y + self.direction[1]

        # Check if the new position is within bounds
        if 0 <= new_x < grid_size and 0 <= new_y < grid_size:
            self.x = new_x
            self.y = new_y
        else:
            self.change_direction()

    def change_direction(self):
        self.direction = random.choice(self.directions)

    def draw(self, screen, cell_size):
        rect = pygame.Rect(self.x * cell_size, self.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, self.color, rect)


class Game:
    def __init__(self, screen, grid_size=10):
        self.screen = screen
        self.grid_size = grid_size
        self.cell_size = self.screen.get_width() // self.grid_size
        self.planes = [Plane(random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)) for _ in range(4)]

    def update(self):
        positions = set()
        for plane in self.planes:
            plane.move(self.grid_size)
            if (plane.x, plane.y) in positions:
                # If a collision is detected, stop the game
                self.planes = []
                break
            positions.add((plane.x, plane.y))

    def draw(self):
        self.screen.fill((0, 0, 0))
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, (255, 255, 255), rect, 1)

        for plane in self.planes:
            plane.draw(self.screen, self.cell_size)
