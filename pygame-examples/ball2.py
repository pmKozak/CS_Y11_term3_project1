import math
import random
from typing import Tuple, List
from paddle2 import Paddle
import pygame


class Ball:
    def __init__(
        self,
        x: float,
        y: float,
        radius: float,
        v: float,
        bearing: float,
        color: Tuple[int, int, int],
    ):
        self.x = x
        self.y = y
        self.v = v
        self.bearing = bearing
        self.radius = radius
        self.color = color

    def update(self, timestep: float, paddles: List[Paddle]):
        boundary_x, boundary_y = pygame.display.get_surface().get_size()

        self.x += self.v * math.cos(self.bearing) * timestep
        self.y += self.v * math.sin(self.bearing) * timestep
        if self.y + self.radius >= boundary_y or self.y - self.radius <= 0:
            self.bearing = 2 * math.pi - self.bearing
        if self.x >= boundary_x:
            # logic for left player getting a point
            print("Point for left player")
            self.restart()
        if self.x <= 0:
            # logic for right player getting a point
            print("Point for right player")
            self.restart()
        for paddle in paddles:
            if (
                    (self.x - self.radius >= paddle.x - paddle.width / 2)
                    or (self.x - self.radius <= paddle.x + paddle.width / 2)
            ) and (
                self.y - self.radius <= paddle.y + paddle.height / 2
            ) and (
                self.y + self.radius >= paddle.y - paddle.height / 2
            ):
                self.bearing = math.pi - self.bearing

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def restart(self):
        boundary_x, boundary_y = pygame.display.get_surface().get_size()
        self.x = boundary_x / 2
        self.y = boundary_y / 2
        self.v = random.randint(30, 50)
        bearing = 1/4
        while 1/8 <= bearing <= 3/8 or 5/8 <= bearing <= 7/8:
            bearing = random.random()
        self.bearing = 2 * math.pi * bearing
