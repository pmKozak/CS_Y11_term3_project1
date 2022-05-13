from typing import Tuple

import pygame


class Object:
    def __init__(
        self,
        x: float,
        y: float,
        height: float,
        width: float,
        v_x: float,
        v_y: float,
        color: Tuple[int, int, int],
    ):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.width = width
        self.height = height
        self.color = color

    def update(self, acceleration: Tuple[float, float], timestep: float):
        boundary_y, boundary_x = pygame.display.get_surface().get_size()
        a_x, a_y = acceleration
        self.v_x += a_x * timestep
        self.v_y += a_y * timestep
        self.x += self.v_x * timestep
        self.y += self.v_y * timestep
        if self.x + self.height / 2 >= boundary_x or self.x - self.height / 2 <= 0:
            self.v_x = -self.v_x
        if self.y + self.width / 2 >= boundary_y or self.y - self.width / 2 <= 0:
            self.v_y = -self.v_y

    def draw(self, surface):
        rect = pygame.Rect(
            self.y - self.width / 2, self.x - self.height / 2, self.width, self.height
        )
        pygame.draw.rect(surface, self.color, rect)