import pygame
import random


class Ball:
    def __init__(self, x, y, radius=10, color=(255, 0, 0), speed=(5, 5)):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed

    def move(self, screen_width, screen_height):
        self.x += self.speed[0]
        self.y += self.speed[1]

        # Bounce off the walls
        if self.x - self.radius < 0 or self.x + self.radius > screen_width:
            self.speed = (-self.speed[0], self.speed[1])
        if self.y - self.radius < 0 or self.y + self.radius > screen_height:
            self.speed = (self.speed[0], -self.speed[1])

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.balls = []
        self.screen_width, self.screen_height = self.screen.get_size()

    def add_ball(self, position):
        radius = random.randint(10, 20)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        speed = (random.choice([-5, 5]), random.choice([-5, 5]))
        ball = Ball(position[0], position[1], radius, color, speed)
        self.balls.append(ball)

    def update(self):
        for ball in self.balls:
            ball.move(self.screen_width, self.screen_height)

    def draw(self):
        self.screen.fill((0, 0, 0))
        for ball in self.balls:
            ball.draw(self.screen)
