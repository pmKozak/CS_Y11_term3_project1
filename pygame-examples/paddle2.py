from typing import Tuple, List

import pygame


class Paddle:
    def __init__(
        self,
        x: float,
        y: float,
        height: float,
        width: float,
        color: Tuple[int, int, int],
        v: float = 0,
        friction: int = 1,
    ):
        self.x = x
        self.y = y
        self.v = v
        self.width = width
        self.height = height
        self.color = color
        assert 1 <= friction <= 100
        self.friction = friction

    def update(self, timestep: float, key_up: bool, key_down: bool):
        boundary_x, boundary_y = pygame.display.get_surface().get_size()
        if key_up:
            self.v -= 1
        if key_down:
            self.v += 1
        self.y += self.v * timestep
        if self.y + self.height / 2 >= boundary_y or self.y - self.height / 2 <= 0:
            self.v = -self.v
        self.v *= (100 - self.friction) / 100

    def draw(self, surface):
        rect = pygame.Rect(
            self.x - self.width / 2, self.y - self.height / 2, self.width, self.height
        )
        pygame.draw.rect(surface, self.color, rect)